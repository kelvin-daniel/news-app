from app import app
import urllib.request,json
from .models import source

Sources = source.Sources
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the base url
base_url = app.config['NEWS_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources (sources_results_list)
    return sources_results

def process_sources(sources_list):
    '''
    function that processes the news results and transform them to a listof objects
    args:
        news_list: a list of dictionaries that contain news details
    returns: news results
    '''
    sources_results= []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        sources_object = Sources(id,name,description,url,category,language,country)
        sources_results.append(sources_object)
    return sources_results
def get_articles(id):
	'''
	Function that processes the articles and returns a list of articles objects
	'''
	get_articles_url = articles_url.format(id,api_key)

	with urllib.request.urlopen(get_articles_url) as url:
		articles_results = json.loads(url.read())

		articles_object = None
		if articles_results['articles']:
			articles_object = process_articles(articles_results['articles'])
	return articles_object

def process_articles(articles_list):
	'''
    Function that processes the news articles results and returns a list of objects
	'''
	articles_object = []
	for article_item in articles_list:
		id = article_item.get('id')
		author = article_item.get('author')
		title = article_item.get('title')
		description = article_item.get('description')
		url = article_item.get('url')
		image = article_item.get('urlToImage')
		date = article_item.get('publishedAt')

		if image:
			articles_result = Articles(id,author,title,description,url,image,date)
			articles_object.append(articles_result)	

	return articles_object
    
def search_article(article_name):
    search_article_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(article_name, api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)

        search_article_results = None

        if search_article_response['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = process_results(search_article_list)


    return search_article_results
