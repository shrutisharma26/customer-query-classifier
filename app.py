from flask import Flask, jsonify, request

from src.predictor import predict_query
from src.database import initialize_database, log_ticket


app = Flask(__name__)


# Initialize database when the application starts
initialize_database()


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "service": "Customer Query Classifier & FAQ Bot",
            "status": "running",
            "endpoint": "POST /predict",
        }
    )


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json(silent=True)

    if not data or "query" not in data:
        return jsonify(
            {
                "error": "Request must contain a 'query' field."
            }
        ), 400

    query = data["query"]

    if not isinstance(query, str) or not query.strip():
        return jsonify(
            {
                "error": "Query must be a non-empty string."
            }
        ), 400

    try:
        result = predict_query(query)

        # Log the classified ticket
        log_ticket(
            result["query"],
            result["intent"],
            result["confidence"],
        )

        return jsonify(result)

    except Exception as error:
        return jsonify(
            {
                "error": str(error)
            }
        ), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
    )