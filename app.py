import requests
from bs4 import BeautifulSoup

def get_forex_news():
    url = "https://www.forexfactory.com/news"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("div", class_="news-article")  # Adjust based on actual structure
    news_list = []

    for article in articles[:5]:  # Get top 5 latest news
        title = article.find("a").text
        link = article.find("a")["href"]
        news_list.append({"title": title, "link": link})

    return news_list

if __name__ == "__main__":
    news = get_forex_news()
    for item in news:
        print(f"{item['title']}: {item['link']}")
