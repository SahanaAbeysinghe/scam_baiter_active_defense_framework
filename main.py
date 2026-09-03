from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timezone
import joblib
import json
import os
import re
import threading
import uuid

from responder import generate_scam_response

app = FastAPI(title="Scam Baiter Active Defense API")

# Load model and vectorizer at startup
model = joblib.load("models/passive_aggressive_detector.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


HISTORY_FILE = "history.json"
HISTORY_MAX_RECORDS = 500
_history_lock = threading.Lock()


def _load_history() -> List[dict]:
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def _save_history(records: List[dict]) -> None:
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(records[-HISTORY_MAX_RECORDS:], f, ensure_ascii=False, indent=2)


def _append_history(record: dict) -> None:
    with _history_lock:
        records = _load_history()
        records.append(record)
        _save_history(records)


def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r'<.*?>', '', text)        # Remove HTML
    text = re.sub(r'[^\w\s]', '', text)      # Match preprocessing used during training
    stop_words = {'the', 'is', 'in', 'and', 'to', 'a', 'of', 'for', 'it', 'on', 'that', 'this', 'with', 'as'}
    text = ' '.join([w for w in text.split() if w not in stop_words])
    return text


class EmailRequest(BaseModel):
    email_text: str


class ScanResponse(BaseModel):
    is_scam: bool
    label: str
    generated_reply: Optional[str] = None


class HistoryRecord(BaseModel):
    id: str
    timestamp: str
    email_text: str
    is_scam: bool
    label: str
    generated_reply: Optional[str] = None


@app.post("/scan", response_model=ScanResponse)
def scan_email(request: EmailRequest):
    raw_text = request.email_text.strip()
    if not raw_text:
        raise HTTPException(status_code=400, detail="email_text cannot be empty.")


    cleaned = clean_text(raw_text)
    vectorized = vectorizer.transform([cleaned])
    prediction = int(model.predict(vectorized)[0])

    is_scam = bool(prediction == 1)
    label = "Phishing/Scam" if is_scam else "Legitimate"
    reply = None

    if is_scam:
        try:
            reply = generate_scam_response(raw_text)
        except Exception as e:
            # Fallback prevents Swagger UI from getting stuck on "LOADING"
            reply = "I received your notification. Could you clarify the steps I should take?"


    _append_history({
        "id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "email_text": raw_text,
        "is_scam": is_scam,
        "label": label,
        "generated_reply": reply,
    })

    return ScanResponse(
        is_scam=is_scam,
        label=label,
        generated_reply=reply
    )


@app.get("/history", response_model=List[HistoryRecord])
def get_history(limit: int = 100):
    """Return past scans, most recent first."""
    records = _load_history()
    records = list(reversed(records))
    if limit:
        records = records[:limit]
    return records


@app.delete("/history")
def clear_history():
    with _history_lock:
        _save_history([])
    return {"status": "cleared"}


@app.get("/")
def health_check():
    return {"status": "running", "message": "Scam Baiter API is live"}