🌐 **News Aggregator via RSS Feed Parser**

A Python-based news scraper that extracts headlines and summaries from over 20 countries using public RSS feeds. The data is structured, language-tagged, and served via a Flask API.

---

### 🚀 Features

* 🌍 Scrapes news from 27 global RSS feeds
* 📄 Extracts structured data: title, summary, date, country, source, and link
* 🈯 Detects language of articles using `langdetect`
* 🌐 Provides a Flask API to access and filter news
* ✅ Handles timeouts, missing fields, and duplicate entries

---

### 📁 Project Structure

```
rss_news_scraper/
├── main.py          → Core script for scraping and saving data  
├── app.py           → Flask API to serve the data  
├── feeds.txt        → List of 20+ RSS feed URLs  
├── output.csv       → Output CSV file with structured news    
├── README.md        → Project documentation  
```

---

### 🛠 Dependencies

Install required libraries:

```
pip install feedparser pandas requests flask langdetect
```

---

### ⚙️ How to Run

**1. Scrape News Data**

```
python main.py
```

This will:

* Load RSS feeds from `feeds.txt`
* Parse and extract article data
* Detect article language
* Save all data to `output.csv`

---

**2. Start the Flask API**

```
python app.py
```

Access the API at:

* [http://127.0.0.1:5000/](http://127.0.0.1:5000/) – Welcome message
* [http://127.0.0.1:5000/news](http://127.0.0.1:5000/news) – All news articles
* [http://127.0.0.1:5000/news?country=India](http://127.0.0.1:5000/news?country=India) – Filter by country
* [http://127.0.0.1:5000/news?lang=en](http://127.0.0.1:5000/news?lang=en) – Filter by language

---

### ✅ Sample Output

| Title          | Source | Country | Language | URL                       |
| -------------- | ------ | ------- | -------- | ------------------------- |
| PM speaks...   | BBC    | UK      | en       | [Link](http://bbc.co.uk/) |
| राहुल गांधी... | TOI    | India   | hi       | [Link](http://toi.in/)    |

---

### 📌 Notes

* Articles are encoded in UTF-8
* Duplicates are automatically removed
* Network failures are handled with timeouts
* Designed to be scalable and extensible

---

### ✨ Bonus Features Implemented

* ✅ Language detection via `langdetect`
* ✅ REST API using Flask to serve filtered news

---

### 🙋‍♀️ Contact

**Raksha Sinha**
For queries or feedback, feel free to connect
LinkedIn - https://www.linkedin.com/in/raksha-sinha-7771b8278/ 
