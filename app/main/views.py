from flask import render_template,request,redirect,url_for
from . import main
from .request import get_sources, get_articles, search_article
from ..models import Sources

#views
@main.route('/')
def index():
    '''
    function that returns the index page and its data
    '''
    # Getting tech news
    news = get_sources('technology')
    title = 'Home- news hub'
    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('search',article_name=search_article))
    else:
        return render_template('index.html',title = title, sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)
#dynamic route
@main.route('/sources/<int:id>')
def articles(id):
    '''
    View articles page function
    '''
    articles = get_articles(id)
    title = f'News-hub || {id}'
    return render_template('news.html',articles = articles, title= title)
@main.route('/everything/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html', articles = searched_articles)
