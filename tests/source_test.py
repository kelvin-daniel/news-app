import unittest
from models import source
Sources = source.Sources

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
if __name__ == '__main__':
    unittest.main()
