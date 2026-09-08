import pickle
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_FILE = BASE_DIR / "model" / "classifier.pkl"
FAQ_FILE = BASE_DIR / "data" / "faq.csv"


# -----------------------------
# LOAD MODEL
# -----------------------------

with MODEL_FILE.open("rb") as file:
    model = pickle.load(file)


# -----------------------------
# LOAD FAQ DATA
# -----------------------------

faq_data = pd.read_csv(FAQ_FILE)

faq_lookup = {
    row["intent"]: {
        "title": row["title"],
        "answer": row["answer"],
    }
    for _, row in faq_data.iterrows()
}


# -----------------------------
# PREDICTION FUNCTION
# -----------------------------

def predict_query(query):
    """
    Classify a customer query and return
    the predicted intent, confidence,
    and matching FAQ.
    """

    if not query or not query.strip():
        raise ValueError("Query cannot be empty.")

    query = query.strip()

    # Predict intent
    prediction = model.predict([query])[0]

    # Get probabilities
    probabilities = model.predict_proba([query])[0]

    # Highest probability
    confidence = max(probabilities)

    # Matching FAQ
    # Low-confidence fallback
    CONFIDENCE_THRESHOLD = 0.55

    if confidence < CONFIDENCE_THRESHOLD:
        prediction = "needs_review"

        faq = {
            "title": "Human Support Review",
            "answer": (
                "We're not confident enough to classify this request. "
                "Please contact customer support so an agent can assist you."
            ),
        }

    else:
        faq = faq_lookup.get(
            prediction,
            {
                "title": "Support",
                "answer": "Please contact customer support for assistance.",
            },
        )

    return {
        "query": query,
        "intent": prediction,
        "confidence": round(float(confidence), 4),
        "faq_title": faq["title"],
        "faq_answer": faq["answer"],
    }


# -----------------------------
# TEST
# -----------------------------

if __name__ == "__main__":

    test_queries = [
        "Why was I charged twice?",
        "The application keeps crashing.",
        "How do I create an account?",
    ]

    for query in test_queries:

        result = predict_query(query)

        print("\n" + "=" * 60)
        print(f"Query:      {result['query']}")
        print(f"Intent:     {result['intent']}")
        print(f"Confidence: {result['confidence']:.2%}")
        print(f"FAQ:        {result['faq_title']}")
        print(f"Answer:     {result['faq_answer']}")