import streamlit as st
import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import plotly.express as px

# Sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return "Positive", score
    elif score <= -0.05:
        return "Negative", score
    else:
        return "Neutral", score

# Fetch news via Google News (scraping)
def fetch_google_news(query, max_items=20):
    url = f"https://news.google.com/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = soup.select("article")[:max_items]
    data = []
    for art in articles:
        title_tag = art.find("a")
        if title_tag:
            title = title_tag.get_text()
            link = "https://news.google.com" + title_tag['href'][1:]
            sentiment, score = get_sentiment(title)
            data.append({"title": title, "url": link, "sentiment": sentiment, "score": score})
    return pd.DataFrame(data)

# Fetch news via NewsAPI
def fetch_newsapi(query, api_key, max_items=20):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&pageSize={max_items}&apiKey=7bdee1423c924023b081298e1edc98d1"
    r = requests.get(url)
    data = r.json()
    articles = data.get("articles", [])
    results = []
    for art in articles:
        title = art.get("title", "")
        url = art.get("url", "#")
        if title:
            sentiment, score = get_sentiment(title)
            results.append({"title": title, "url": url, "sentiment": sentiment, "score": score})
    return pd.DataFrame(results)

# Streamlit UI 
st.set_page_config(page_title="Real-time Sentiment Dashboard", layout="wide")
st.title("📰 Real-time Sentiment Analysis Dashboard")

# Input fields
source = st.radio("Select Data Source:", ["Google News (Scraping)", "NewsAPI"])
query = st.text_input("Enter a topic (e.g., Tesla, Cricket, AI):", "Artificial Intelligence")
api_key = None

if source == "NewsAPI":
    api_key = st.text_input("Enter your NewsAPI Key:", type="password")

if st.button("Fetch Data"):
    with st.spinner("Fetching news..."):
        if source == "Google News (Scraping)":
            df = fetch_google_news(query, max_items=30)
        else:
            if not api_key:
                st.error("⚠ Please enter your NewsAPI key.")
                st.stop()
            df = fetch_newsapi(query, api_key, max_items=30)

        if not df.empty:
            # Metrics
            total = len(df)
            pos = (df['sentiment'] == "Positive").sum()
            neg = (df['sentiment'] == "Negative").sum()
            neu = (df['sentiment'] == "Neutral").sum()

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Articles", total)
            col2.metric("Positive %", f"{(pos/total)*100:.1f}%")
            col3.metric("Negative %", f"{(neg/total)*100:.1f}%")

            # Pie chart
            fig = px.pie(df, names="sentiment", title="Sentiment Breakdown", hole=0.4)
            st.plotly_chart(fig, use_container_width=True)

            # Show articles
            st.subheader("Recent Mentions")
            for _, row in df.iterrows():
                st.markdown(
                    f"{row['title']}**  \n"
                    f"[Read more]({row['url']})  \n"
                    f"Sentiment: {row['sentiment']}  \n---"
                )
        else:
            st.warning("No articles found for your query.")