import requests


API_URL = "http://127.0.0.1:5000/predict"


test_queries = [
    "Why was I charged twice for my order?",
    "The application keeps crashing when I open it.",
    "How do I create an account?",
    "My payment was declined.",
    "I cannot upload my document.",
    "Where can I contact customer support?",
]


for query in test_queries:

    response = requests.post(
        API_URL,
        json={"query": query},
        timeout=10,
    )

    print("\n" + "=" * 60)
    print(f"Query:      {query}")
    print(f"Status:     {response.status_code}")

    if response.ok:
        result = response.json()

        print(f"Intent:     {result['intent']}")
        print(f"Confidence: {result['confidence']:.2%}")
        print(f"FAQ:        {result['faq_title']}")

    else:
        print("Error:", response.text)