from flask import render_template
from app import app
from .request import get_news


# Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     message = 'NEWS HIGHLIGHT'
#     return render_template('index.html',message = message)

# Views
@app.route("/")
def index():#define our function
    top_news=news("top-headlines")#top-headlines is the parameter that our api will join it with the key
    print(top_news)
    
    return render_template("index.html",top_headline=top_news) 

    
    description: "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com."
    

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)

def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title)  

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    popular_news = get_news('popular')
    print(popular_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title,popular = popular_news)

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    popular_news = get_news('popular')
    upcoming_news = get_news('upcoming')
    now_showing_news = get_news('now_playing')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news )


