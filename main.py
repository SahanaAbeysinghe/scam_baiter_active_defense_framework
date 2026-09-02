from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import joblib
import re

from responder import generate_scam_response

app = FastAPI(title="Scam Baiter Active Defense API")

# Load model and vectorizer at startup
model = joblib.load("models/passive_aggressive_detector.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


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


@app.post("/scan", response_model=ScanResponse)
def scan_email(request: EmailRequest):
    raw_text = request.email_text.strip()
    if not raw_text:
        raise HTTPException(status_code=400, detail="email_text cannot be empty.")

    # Feature transformation & classification
    cleaned = clean_text(raw_text)
    vectorized = vectorizer.transform([cleaned])
    prediction = int(model.predict(vectorized)[0])

    is_scam = bool(prediction == 1)
    reply = None

    if is_scam:
        try:
            reply = generate_scam_response(raw_text)
        except Exception as e:
            # Fallback prevents Swagger UI from getting stuck on "LOADING"
            reply = "I received your notification. Could you clarify the steps I should take?"

    return ScanResponse(
        is_scam=is_scam,
        label="Phishing/Scam" if is_scam else "Legitimate",
        generated_reply=reply
    )


@app.get("/")
def health_check():
    return {"status": "running", "message": "Scam Baiter API is live"}