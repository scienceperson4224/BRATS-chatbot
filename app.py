from flask import Flask, render_template, request, jsonify
from echo import explain

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # check if text is valid
    response = explain(target=text, context="Chat user message")
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)