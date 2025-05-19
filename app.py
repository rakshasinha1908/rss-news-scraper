from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load news data from CSV
def load_data():
    try:
        df = pd.read_csv("output.csv", encoding="utf-8")
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return []

# Home route
@app.route("/")
def home():
    return {"message": "Welcome to the News API. Use /news to get data."}

# API to get all news or filter by country/language
@app.route("/news", methods=["GET"])
def get_news():
    country = request.args.get("country")
    language = request.args.get("lang")

    data = load_data()

    if country:
        data = [article for article in data if str(article.get("Country", "")).lower() == country.lower()]
    if language:
        data = [article for article in data if str(article.get("Language", "")).lower() == language.lower()]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
