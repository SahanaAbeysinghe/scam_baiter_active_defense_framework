Markdown
# 🛡️ Scam-Baiter Active Defense Framework

An end-to-end cybersecurity tool that classifies incoming text for phishing signatures and automatically deploys generative AI countermeasures to waste scammers' time. 

This project bridges a data science machine learning pipeline with a functional FastAPI backend and a custom-styled Streamlit frontend, providing a complete platform for intent verification and active defense.

## 🚀 Core Features
* **Machine Learning Classification:** Utilizes a `PassiveAggressiveClassifier` and TF-IDF vectorization to detect malicious intent with high accuracy, trained on a strictly sanitized 10k+ row dataset.
* **Generative Countermeasures:** Integrates the `google-genai` SDK (Gemini 3.5-flash-lite) to dynamically generate believable, time-wasting responses to confirmed phishing attempts.
* **Robust API Backend:** Built with FastAPI, featuring synchronous routing and fallback exception handling to prevent network timeouts during LLM latency spikes.
* **Modern UI/UX:** A custom-styled Streamlit frontend featuring dark-mode neon aesthetics, dynamic metric dashboards, and real-time threat reporting.

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Frontend:** Streamlit, CSS
* **Machine Learning:** Scikit-learn, Pandas, Joblib
* **Generative AI:** Google GenAI SDK (Gemini 3.5-flash-lite)

## 📁 Repository Structure
```text
├── models/
│   ├── passive_aggressive_detector.pkl  # Trained ML model
│   └── tfidf_vectorizer.pkl             # Fitted vectorizer
├── evaluation/
│   ├── evaluate_model.py                # Model evaluation & confusion matrix script
│   └── scam_baiter_confusion_matrix.png # Evaluation results visualization
├── .env                                 # Environment variables (API keys)
├── app.py                               # Streamlit frontend UI
├── main.py                              # FastAPI server and endpoints
├── responder.py                         # Google GenAI integration logic
├── requirements.txt                     # Project dependencies
└── README.md                            # Documentation
```

## ⚙️ Local Setup & Installation
```text
1. Clone the repository and initialize the environment
Bash
git clone [https://github.com/yourusername/scam-baiter-active-defense.git](https://github.com/yourusername/scam-baiter-active-defense.git)
cd scam-baiter-active-defense
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

2. Install dependencies
Bash
pip install -r requirements.txt

3. Configure Environment Variables
Create a .env file in the root directory and add your Google Gemini API key:
Code snippet
GEMINI_API_KEY=your_api_key_here

4. Launch the Application
You will need two terminal windows to run the backend and frontend concurrently.

Terminal 1 (FastAPI Backend):
Bash
uvicorn main:app --reload

Terminal 2 (Streamlit Frontend):
Bash
streamlit run app.py

📡 API Documentation
When the backend is running, the interactive Swagger UI is available at http://127.0.0.1:8000/docs.
Endpoint: POST /scan
Evaluates text for phishing signatures and returns classification data alongside an optional generated countermeasure.

Request Body:

JSON
{
  "email_text": "URGENT: Your account has been locked. Verify your identity immediately."
}
Response:

JSON
{
  "is_scam": true,
  "label": "Phishing/Scam",
  "generated_reply": "Oh my, I definitely don't want my account locked. What exact steps do I need to take to fix this?"
}
```

## 📊 Model Evaluation

The deployed detector (Passive Aggressive Classifier + TF-IDF) was evaluated on a held-out
20% test split from the training dataset, using the exact same preprocessing pipeline and
random seed as training to ensure the test set was never seen by the model during fitting.

### Dataset
Trained and evaluated on the combined phishing/legitimate email corpus
([`naserabdullahalam/phishing-email-dataset`](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset)
on Kaggle — "Phish No More", merging Enron, Ling, CEAS, Nazario, Nigerian Fraud, and
SpamAssassin corpora). The raw CSV (~100MB) is not committed to this repo — download it from
Kaggle and place it in the project root as `phishing_email.csv` before running the evaluation
script.

### Results

| Metric | Legitimate | Scam | Overall |
|---|---|---|---|
| Precision | 0.98 | 0.98 | 0.98 |
| Recall | 0.98 | 0.98 | 0.98 |
| F1-Score | 0.98 | 0.98 | 0.98 |
| Support | 7,847 | 8,567 | 16,414 |

**Overall accuracy: 98%** — Average inference latency: 0.122 ms/email

**Confusion Matrix:**

![Confusion Matrix](evaluation/scam_baiter_confusion_matrix.png)

|  | Predicted: Legitimate | Predicted: Scam |
|---|---|---|
| **Actual: Legitimate** | 7,692 | 155 |
| **Actual: Scam** | 146 | 8,421 |

A comparison across all 10 trained models (Naive Bayes, Logistic Regression, LinearSVC,
Random Forest, Complement NB, SGD, Passive Aggressive, MLP, Ridge, Extra Trees) is available
in the training notebook. Passive Aggressive was selected for deployment as the best
accuracy-to-latency tradeoff (98.17% accuracy at ~3ms prediction time, vs. Extra Trees'
marginally higher 98.88% accuracy at ~1,300ms and 123MB model size).

### Reproducing this evaluation
```bash
python evaluation/evaluate_model.py
```
Requires `phishing_email.csv` in the project root and the trained model artifacts in
`models/` (already included in this repo).

### Note on methodology
An earlier version of this evaluation script produced a false 100% accuracy result due to a
train/test split mismatch — the script deduplicated after splitting rather than before,
causing ~79% of the "test" set to unintentionally overlap with the model's actual training
data. This was caught by cross-checking against the original training pipeline's methodology
and corrected before finalizing these results.

## Developer: SahanaAbeysinghe
