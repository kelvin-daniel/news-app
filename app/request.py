from app import app
import urllib.request,json
from .models import movie

News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(sources,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)
    return news_results

def process_results(news_list):
    '''
    function that processes the news results and transform them to a listof objects
    args:
        news_list: a list of dictionaries that contain news details
    returns: news results
    '''
    news_results= []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if name:
            movie_object = Movie(id,name,description,url,category,language,country)
            news_results.append(news_object)

    return news_results