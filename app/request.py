from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news():
    get_news_url=base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)

        news_results=None

        if get_news_response['sources']:#getting our data from the Api
            news_result_list=get_news_response["sources"]
            news_results=process_results(news_result_list)

    return news_results

def process_results(news_list):
    news_results = []
    for news_item in news_list:
        id=news_item.get("id")
        name = news_item.get("name")
        description=news_item.get("description")
        url=news_item.get("url")
        category=news_item.get("category")
        language=news_item.get("language")
        country=news_item.get("country")

        news_object=News(id,name,description,url,category,language,country)

        news_results.append(news_object)
        
    return news_results






