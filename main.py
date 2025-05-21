# Required libraries for parsing, language detection, and data handling

import requests
import feedparser
import pandas as pd
from langdetect import detect, DetectorFactory

# Ensure consistent language detection results
DetectorFactory.seed = 0  

# Mapping of domain names to their respective country and news agency
feed_sources = {
    "bbc.co.uk": ("UK", "BBC"),
    "cnn.com": ("USA", "CNN"),
    "npr.org": ("USA", "NPR"),
    "nytimes.com": ("USA", "NYTimes"),
    "aljazeera.com": ("Middle East", "Al Jazeera"),
    "timesofindia.indiatimes.com": ("India", "TOI"),
    "hindustantimes.com": ("India", "Hindustan Times"),
    "nhk.or.jp": ("Japan", "NHK"),
    "cbc.ca": ("Canada", "CBC"),
    "abc.net.au": ("Australia", "ABC Australia"),
    "dw.com": ("Germany", "DW"),
    "lemonde.fr": ("France", "Le Monde"),
    "tass.com": ("Russia", "TASS"),
    "chinadaily.com.cn": ("China", "China Daily"),
    "koreatimes.co.kr": ("South Korea", "Korea Times"),
    "straitstimes.com": ("Singapore", "Straits Times"),
    "thestar.com.my": ("Malaysia", "The Star"),
    "thejakartapost.com": ("Indonesia", "Jakarta Post"),
    "g1.globo.com": ("Brazil", "G1"),
    "news24.com": ("South Africa", "News24"),
    "mexiconewsdaily.com": ("Mexico", "Mexico News Daily"),
    "gulfnews.com": ("UAE", "Gulf News"),
    "dawn.com": ("Pakistan", "Dawn"),
    "thedailystar.net": ("Bangladesh", "Daily Star"),
    "philstar.com": ("Philippines", "PhilStar"),
    "hurriyetdailynews.com": ("Turkey", "Hurriyet"),
    "ansa.it": ("Italy", "ANSA"),
}

# Load RSS feed URLs from feeds.txt
try:
    with open("feeds.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]
except FileNotFoundError:
    print("❌ Error: 'feeds.txt' file not found.")
    exit()

# Exit if no valid URLs are found
if not urls:
    print("⚠️ No RSS feed URLs found in feeds.txt.")
    exit()

print(f"✅ Loaded {len(urls)} RSS feed URLs.")

articles = []

# Loop through each RSS feed URL and parse its content
for url in urls:
    print(f"\n🔄 Parsing: {url}")
    try:
        feed = feedparser.parse(url)
        print(f"📰 Found {len(feed.entries)} articles")

        for entry in feed.entries:
            # Try to infer the country and source from the feed URL
            source_url = feed.href if 'href' in feed else url
            matched = [(c, s) for domain, (c, s) in feed_sources.items() if domain in source_url]
            country, source = matched[0] if matched else ("Unknown", "Unknown")
            
            # Extract article title and summary
            title = entry.get("title", "")
            summary = entry.get("summary", "")
            text_to_detect = f"{title} {summary}".strip()
            
            # Detect language of the combined text
            try:
                language = detect(text_to_detect) if text_to_detect else "unknown"
            except:
                language = "unknown"
                
            # Append structured article data
            articles.append({
                "Title": title or "N/A",
                "Publication Date": entry.get("published", "N/A"),
                "Summary": summary or "N/A",
                "URL": entry.get("link", "N/A"),
                "Source": source,
                "Country": country,
                "Language": language
            })


    except Exception as e:
        print(f"❌ Failed to parse {url} — {e}")

# Convert to DataFrame and remove duplicates
df = pd.DataFrame(articles)
df.drop_duplicates(subset=["Title", "URL"], inplace=True)

# Save final output to CSV
if not df.empty:
    df.to_csv("output.csv", index=False, encoding="utf-8")
    print(f"\n✅ Successfully saved {len(df)} articles to output.csv")
else:
    print("\n⚠️ No articles were parsed. Please check RSS URLs and try again.")
    

# To Generate summary table
summary = df.groupby(["Country", "Source"]).size().reset_index(name="Total Articles")
summary["Total Historical Data"] = "Current Feed Only"  

# Save to CSV
summary.to_csv("summary_table.csv", index=False)
print("\n📊 Summary table saved as summary_table.csv")


# -------------------------
# NOTE:
# Although feeds.txt contains 27 RSS feed URLs from various countries,
# the final summary table may include fewer sources. This happens because:
# - Some feeds return no articles (inactive or empty)
# - Some feeds fail to parse due to connection errors or timeouts
# - Duplicate articles (based on Title and URL) are removed
# - Only feeds that successfully return valid articles are included
# As a result, the summary table reflects only the data-producing sources.
# -------------------------

