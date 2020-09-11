import unittest
from app.models import Sources,Articles

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(1234,'ABC News','description','"http://www.abc.net.au/news"','general','en','au')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))
class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('CNN','joe','Big five','The wilds biggest creatures you dont want to encounter at night','kws.com','kws.com/wild1.png','2020-11-11T13:57:16Z')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

