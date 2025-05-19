```markdown
# 🌐 News Aggregator via RSS Feed Parser

This project is a Python-based RSS feed scraper that extracts and serves news articles from over 20 countries using public RSS feeds. It stores the data, detects language, and exposes it via a Flask API.

---

## 🚀 Features

- 🔎 Scrapes news from 27 global RSS feeds
- 📰 Extracts structured data: title, summary, publication date, country, source, link
- 🌍 Detects language of articles
- 🌐 Flask API to access and filter news
- ✅ Handles timeouts, missing fields, and duplicate articles

---

## 📁 Project Structure

```

rss\_news\_scraper/
├── main.py          # Core script for scraping and saving data
├── app.py           # Flask API to serve the data
├── feeds.txt        # List of 20+ RSS feed URLs
├── output.csv       # Output CSV file with structured news
├── utils.py         # (Optional) Helper functions for modular code
├── README.md        # Project documentation

````

---

## 🛠 Dependencies

Install required libraries using:

```bash
pip install feedparser pandas requests flask langdetect
````

---

## ⚙️ How to Run

### 1. Scrape News Data

```bash
python main.py
```

This will:

* Load RSS feeds from `feeds.txt`
* Parse and extract article info
* Save results to `output.csv` with language detection

---

### 2. Start the Flask API

```bash
python app.py
```

Then open in your browser:

* `http://127.0.0.1:5000/` – Welcome message
* `http://127.0.0.1:5000/news` – All news
* `http://127.0.0.1:5000/news?country=India` – Filter by country
* `http://127.0.0.1:5000/news?lang=en` – Filter by language

---

## ✅ Sample Output

| Title            | Source | Country | Language | URL                                       |
| ---------------- | ------ | ------- | -------- | ----------------------------------------- |
| "PM speaks..."   | BBC    | UK      | en       | [http://bbc.co.uk/](http://bbc.co.uk/)... |
| "राहुल गांधी..." | TOI    | India   | hi       | [http://toi.in/](http://toi.in/)...       |

---

## 💡 Notes

* All articles are stored in UTF-8 encoding.
* Duplicate and empty entries are filtered automatically.
* Timeouts prevent the script from hanging on slow feeds.

---

## 📌 Optional Enhancements Implemented

* [x] Language detection using `langdetect`
* [x] Flask API to serve and filter news

---

## 📬 Contact

**Raksha Sinha**
For queries or feedback, feel free to reach out.

```


