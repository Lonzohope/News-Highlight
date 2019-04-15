from flask import render_template
from app import app
from .request import get_news


@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    popular_news = get_news("top-headlines")
    # upcoming_news = get_news()
    # now_showing_news = get_news()
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', topnews=popular_news)


