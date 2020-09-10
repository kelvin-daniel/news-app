from app import app
import urllib.request,json
from .models import news

News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the base url
base_url = app.config['NEWS_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        news_results = None

        if get_sources_response['sources']:
            news_results_list = get_sources_response['sources']
            sources_results = process_sources (news_sources_list)
    return sources_results

def process_sources(sources_list):
    '''
    function that processes the news results and transform them to a listof objects
    args:
        news_list: a list of dictionaries that contain news details
    returns: news results
    '''
    sources_results= []
    for news_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

        if name:
            sources_object = News(id,name,description,url,category,language,country)
            sources_results.append(sources_object)

    return sources_results