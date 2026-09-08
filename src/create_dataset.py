import csv
import random
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)


examples = {
    "billing": [
        "Why was I charged twice for the same order?",
        "I was billed twice for one purchase.",
        "There is a duplicate charge on my account.",
        "Why did I get charged two times?",
        "I don't recognize this charge on my card.",
        "There is a payment I did not make.",
        "I see an unfamiliar transaction on my account.",
        "Can you explain this charge on my account?",
        "Why is my invoice higher than expected?",
        "The amount on my bill is incorrect.",
        "I was charged more than the displayed price.",
        "My bill has an incorrect amount.",
        "How can I get a refund?",
        "I want to request a refund for my purchase.",
        "Can you help me get my money back?",
        "I need to cancel a payment and get a refund.",
        "When will my refund arrive?",
        "How long does a refund take?",
        "My refund has not appeared yet.",
        "I am still waiting for my refunded money.",
        "What payment methods do you accept?",
        "Can I pay using a credit card?",
        "Do you support debit card payments?",
        "Can I use another payment method?",
        "My payment was declined.",
        "Why did my card payment fail?",
        "The payment keeps getting rejected.",
        "I cannot complete my payment.",
        "How do I update my billing information?",
        "I need to change my payment details.",
    ],
    "technical": [
        "The app keeps crashing when I open it.",
        "Why does the application close unexpectedly?",
        "The app crashes every time I try to use it.",
        "I am getting an error when opening the app.",
        "The website is not loading.",
        "The page keeps showing an error.",
        "I cannot access the website.",
        "The site is completely unresponsive.",
        "I forgot my password and cannot log in.",
        "I am unable to sign into my account.",
        "Login is not working for me.",
        "I cannot access my account.",
        "The verification code is not arriving.",
        "I did not receive the OTP.",
        "The login code never reached my phone.",
        "I am not receiving the verification email.",
        "The application is extremely slow.",
        "Why is the website so slow?",
        "Pages are taking too long to load.",
        "The system is responding very slowly.",
        "I cannot upload my file.",
        "The upload keeps failing.",
        "Why won't my document upload?",
        "I am having trouble uploading a file.",
        "The search feature is not working.",
        "Search results are not appearing.",
        "The search button does nothing.",
        "I cannot find anything using search.",
        "The app is showing a technical error.",
        "Something seems to be broken with the application.",
    ],
    "general": [
        "What are your customer support hours?",
        "When can I contact customer support?",
        "How do I contact support?",
        "Where can I reach your support team?",
        "What services do you provide?",
        "Can you tell me what your service offers?",
        "What can I use this platform for?",
        "I want to learn more about your services.",
        "How do I create an account?",
        "Where can I sign up?",
        "How can I register for an account?",
        "What are the steps to create an account?",
        "Can I change my account information?",
        "How do I update my profile?",
        "Where can I edit my account details?",
        "I want to change my personal information.",
        "Do you have a mobile application?",
        "Is there an app I can use?",
        "Can I use the service on my phone?",
        "Do you offer a mobile version?",
        "Where can I find your terms and conditions?",
        "How can I read your terms of service?",
        "Where are the company policies listed?",
        "I want to know more about your policies.",
        "How do I close my account?",
        "I want to delete my account.",
        "Can I permanently remove my account?",
        "What is the process for closing an account?",
        "Where can I find more information?",
        "Can someone explain how the service works?",
    ],
}


rows = []

for intent, queries in examples.items():
    for query in queries:
        rows.append((query, intent))


random.seed(42)
random.shuffle(rows)


output_file = DATA_DIR / "queries.csv"

with output_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["query", "intent"])
    writer.writerows(rows)


faq_data = [
    [
        "billing",
        "Billing & Payments",
        "For billing questions, duplicate charges, refunds, and payment issues, please review your billing details or contact support.",
    ],
    [
        "technical",
        "Technical Support",
        "For technical problems, try restarting the application and checking your connection. If the issue continues, contact technical support.",
    ],
    [
        "general",
        "General Information",
        "For general questions about accounts, services, policies, and support, please check the relevant help section or contact support.",
    ],
]


faq_file = DATA_DIR / "faq.csv"

with faq_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["intent", "title", "answer"])
    writer.writerows(faq_data)


print(f"Created: {output_file}")
print(f"Created: {faq_file}")
print(f"Total queries: {len(rows)}")