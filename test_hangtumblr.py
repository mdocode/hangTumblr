import unittest
from hangblogs import HangPost
import tumblr

class TestHangpost(unittest.TestCase):

    def testHangPostFromDict(self):
        api = tumblr.Api('testy-workpls')
        d = api.read(id=17390096011)
        hp = HangPost(d)
        unittest.assertEqual(hp.id, 17390096011)
        unittest.assertEqual(hp.photo, 'http://27.media.tumblr.com/tumblr_lz6q0gDfhG1qh3h2lo1_500.jpg')
        unittest.assertEqual(hp.tags, [u'i wish', u'tagssss', u'whee'])
        
if __name__ == '__main__':
    unittest.main()

