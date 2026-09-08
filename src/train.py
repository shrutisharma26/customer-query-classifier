import pandas as pd
import pickle

from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "queries.csv"
MODEL_DIR = BASE_DIR / "model"

MODEL_DIR.mkdir(exist_ok=True)


# -----------------------------
# LOAD DATA
# -----------------------------

data = pd.read_csv(DATA_FILE)

X = data["query"]
y = data["intent"]


print(f"Total samples: {len(data)}")
print("\nClass distribution:")
print(y.value_counts())


# -----------------------------
# TRAIN / TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)


print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# -----------------------------
# ML PIPELINE
# -----------------------------

pipeline = Pipeline(
    [
        (
            "tfidf",
            TfidfVectorizer(
                lowercase=True,
                stop_words="english",
                ngram_range=(1, 2),
                sublinear_tf=True,
            ),
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                random_state=42,
            ),
        ),
    ]
)


# -----------------------------
# TRAIN
# -----------------------------

print("\nTraining model...")

pipeline.fit(X_train, y_train)


# -----------------------------
# EVALUATE
# -----------------------------

y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 50)
print("MODEL EVALUATION")
print("=" * 50)

print(f"\nAccuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# -----------------------------
# SAVE MODEL
# -----------------------------

model_file = MODEL_DIR / "classifier.pkl"

with model_file.open("wb") as file:
    pickle.dump(pipeline, file)


print("=" * 50)
print(f"Model saved to: {model_file}")
print("=" * 50)