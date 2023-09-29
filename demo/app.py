from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
intent_classifier = joblib.load("./intent_classifier.joblib")

@app.route("/")
def homepage():
    return "Hello World"


@app.route("/get-intent", methods=["POST"])
def intent_recognition():
    text = request.form.get("sentence")
    intent = intent_classifier.predict([text])
    response = {"intent" : str(intent[0])}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=19566)
