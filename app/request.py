from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(newsnow):
    get_news_url=base_url.format(newsnow,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)

        news_results=None

        if get_news_response['articles']:#getting our data from the Api
            news_result_list=get_news_response["articles"]
            news_results=process_results(news_result_list)

    return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        id=news_item.get("title")
        name=news_item.get("name")
        author=news_item.get("author")
        title=news_item.get("title")
        description=news_item.get("description")
        url=news_item.get("url")
        urlToImage=news_item.get("urlToImage")
        publishedAt=news_item.get("publishedAt")
        content=news_item.get("content")
        
        news_object=News(title)

        news_results.append(news_object)
        
    return news_results






