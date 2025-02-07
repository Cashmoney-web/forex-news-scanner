import requests
from bs4 import BeautifulSoup

# Import Telegram function
from telegram_alert import send_telegram_message

def get_forex_news():
    url = "https://www.forexfactory.com/news"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("div", class_="news-article")  # Adjust this based on actual site structure
    news_list = []

    for article in articles[:3]:  # Get top 3 latest news
        title = article.find("a").text
        link = article.find("a")["href"]
        news_list.append(f"📢 {title}\n🔗 {link}")

    return news_list

# Fetch news and send to Telegram
news = get_forex_news()
for item in news:
    send_telegram_message(item)
