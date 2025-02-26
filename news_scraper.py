import requests
from bs4 import BeautifulSoup

def get_latest_news():
    url = "https://www.ign.com/news"  # Nguồn tin tức
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    news_list = []

    articles = soup.find_all("div", class_="news-article")[:5]  # Lấy 5 tin đầu
    for article in articles:
        title = article.find("h3").text
        link = article.find("a")["href"]
        news_list.append({"title": title, "link": link})

    return news_list