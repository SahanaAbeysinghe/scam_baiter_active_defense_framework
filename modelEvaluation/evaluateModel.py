import time
import re
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('phishing_email.csv')

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'http\S+|www\.\S+', ' url ', text)
    text = re.sub(r'[^\w\s]', '', text)
    stop_words = set(['the', 'is', 'in', 'and', 'to', 'a', 'of', 'for', 'it', 'on', 'that', 'this', 'with', 'as'])
    text = ' '.join([w for w in text.split() if w not in stop_words])
    return text

df['cleaned_text'] = df['text_combined'].apply(clean_text)

# CRITICAL: dedupe BEFORE splitting — this must match the original training
# pipeline exactly, or train_test_split produces a different split entirely
# and "test" rows leak into what the model was actually trained on.
df_deduped = df.drop_duplicates(subset=['cleaned_text']).copy()

X_train, X_test_raw, y_train, y_true = train_test_split(
    df_deduped['cleaned_text'],
    df_deduped['label'],
    test_size=0.2,
    random_state=42,
    stratify=df_deduped['label']
)

vectorizer = joblib.load('models/tfidf_vectorizer.pkl')
classifier = joblib.load('models/passive_aggressive_detector.pkl')

start_time = time.time()
X_test_vectorized = vectorizer.transform(X_test_raw)
y_pred = classifier.predict(X_test_vectorized)
end_time = time.time()

total_time_ms = (end_time - start_time) * 1000
avg_latency_ms = total_time_ms / len(y_true)

print("=== Scam-Baiter Defense Engine Evaluation ===")
print(f"Total Test Samples Evaluated: {len(y_true)}")
print(f"Average Pipeline Latency: {avg_latency_ms:.3f} ms / email\n")

print("--- Classification Report ---")
print(classification_report(y_true, y_pred, target_names=["Legitimate", "Scam"]))

cm = confusion_matrix(y_true, y_pred)
print("\n--- Confusion Matrix ---")
print(cm)

plt.figure(figsize=(7, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens',
            xticklabels=["Legitimate", "Scam"],
            yticklabels=["Legitimate", "Scam"])
plt.title('Threat Detection Confusion Matrix')
plt.ylabel('Actual Classification')
plt.xlabel('Predicted Classification')
plt.savefig('scam_baiter_confusion_matrix.png', dpi=300, bbox_inches='tight')

print("\nSaved 'scam_baiter_confusion_matrix.png' to project root.")