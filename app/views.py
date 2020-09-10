from flask import render_template
from app import app
from .request import get_news

#views
@app.route('/')
def index():
    '''
    function that returns the index page and its data
    '''
    # Getting tech news
    news = get_news('technology')
    title = 'Home- news hub'
    return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)
#dynamic route
@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    title = 'News-hub'
    return render_template('news.html',id = news_id, title= title)

