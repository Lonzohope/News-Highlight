import urllib.request
import json
from .models import news, articles

News = news.News
Source = articles.Sources

Articles = articles.Articles
# Getting api key
api_key = None
base_url = None
source_url = None
article_url = None

# Getting the news base url
def configure_request(app):
    global base_url, source_url, article_url, api_key
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_API_BASE_URL"]
    source_url = app.config["SOURCE_API"]
    article_url = app.config["ARTICLE_URL"]


def get_news(newsnow):
    get_news_url = base_url.format(newsnow, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:  # getting our data from the Api
            news_result_list = get_news_response["articles"]
            news_results = process_results(news_result_list)

    return news_results


def process_results(news_list):
    news_results = []
    for news_item in news_list:
        title = news_item.get("title")
        description = news_item.get("description")
        url = news_item.get("url")
        urlToImage = news_item.get("urlToImage")
        publishedAt = news_item.get("publishedAt")
        if title and urlToImage:
            news_object = News(title, description, url,
                               urlToImage, publishedAt)
            news_results.append(news_object)
            news_results = news_results[0:12]

    return news_results


def get_sources(source):
    get_source_url = source_url.format(source, api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:  # getting our data from the Api
            source_result_list = get_source_response["sources"]
            source_results = process_result(source_result_list)

    return source_results


def process_result(source_list):
    source_results = []
    for source in source_list:
        id = source.get("id")
        name = source.get("name")
        url = source.get("url")

        source_obj = Source(id, name, url)
        source_results.append(source_obj)
        source_results = source_results[0:4]
    return source_results


# geting the articles
