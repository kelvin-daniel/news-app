from flask import render_template
from app import app
from .request import get_sources, get_articles

#views
@app.route('/')
def index():
    '''
    function that returns the index page and its data
    '''
    # Getting tech news
    news = get_sources('technology')
    title = 'Home- news hub'
    return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)
#dynamic route
@app.route('/sources/<int:news_id>')
def news(id):
    '''
    View articles page function
    '''
    articles = get_articles(id)
    title = f'News-hub || {id}'
    return render_template('news.html',articles = articles, title= title)

