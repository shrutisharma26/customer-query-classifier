# Customer Query Classifier & FAQ Bot

An NLP-powered customer support backend that automatically classifies customer queries into predefined support categories and returns a relevant FAQ response.

The system combines **TF-IDF**, **Logistic Regression**, **confidence-based fallback handling**, **SQLite**, and a **Flask REST API**.

---

## Overview

Customer support teams receive large numbers of repetitive queries. This project demonstrates a lightweight NLP pipeline that can automatically identify the intent behind a customer query and provide an appropriate FAQ response.

### Pipeline

Customer Query
↓
TF-IDF Feature Extraction
↓
Logistic Regression Classifier
↓
Intent + Confidence Score
↓
FAQ Retrieval
↓
SQLite Ticket Logging
↓
Flask REST API

---

## Features

- NLP-based customer query classification
- TF-IDF feature extraction
- Logistic Regression classification
- Three support intent categories:
  - Billing
  - Technical
  - General
- Confidence score for every prediction
- Low-confidence fallback to human support
- FAQ retrieval based on predicted intent
- SQLite database for ticket logging
- REST API built with Flask
- Automated API testing with Python Requests

---

## Machine Learning

### Dataset

The project uses a curated synthetic customer-support dataset containing:

- **90 customer queries**
- **3 intent categories**
- **30 examples per category**

The dataset is split into:

- 80% training data
- 20% test data

A fixed random seed and stratified split are used to keep the evaluation reproducible and maintain class balance.

### Text Representation

Customer queries are converted into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

The implementation uses:

- lowercase text
- English stop-word removal
- unigram and bigram features
- sublinear TF scaling

### Classifier

A **Logistic Regression** classifier is trained on the TF-IDF features.

The model produces both:

- predicted intent
- class probability used as a confidence score

---

## Model Evaluation

The model was evaluated on a held-out test set of 18 queries.

| Metric | Score |
|---|---:|
| Accuracy | 83.33% |
| Billing F1-score | 0.86 |
| General F1-score | 0.80 |
| Technical F1-score | 0.83 |
| Macro F1-score | 0.83 |

The dataset is synthetic and relatively small, so these results should not be interpreted as production-level performance.

---

## Confidence-Based Fallback

The classifier does not blindly assign every query to an intent.

A confidence threshold of **55%** is used.

If the predicted confidence is below the threshold, the system returns:

```text
needs_review