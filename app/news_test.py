import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'Holy SMokes','A must read article','https://url.newsapi.org/v2/sources',8.5,129993)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
if __name__ == '__main__':
    unittest.main()
