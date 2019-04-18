from flask import render_template
from app import app
from .request import get_news,get_sources


@app.route('/news/<name>')
def news(name):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',name=name)


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    sources=get_sources("sources")
    # Getting popular news
    popular_news = get_news("top-headlines")
    # upcoming_news = get_news()
    # now_showing_news = get_news()
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', topnews=popular_news,tpsource=sources)


