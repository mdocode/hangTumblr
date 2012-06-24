from tumblr import Api
from random import random, shuffle

class HangPost(object):
    def __init__(self, tumblrBlogDict):
        self.id = tumblrBlogDict['id']
        self.photo = (tumblrBlogDict['photo-url-500'])
        self.tags = tumblrBlogDict['tags']

class ImageTagBlog(object):
    def __init__(self, blogname):
        self.url = blogname
        try:
            listOfPosts = image_posts_with_tags(self.url)
            self.hangPosts = [HangPost(tbDict) for tbDict in listOfPosts]
        except:
            self.hangPosts = None;
            print "error retrieving blog posts"

        
def image_posts_with_tags(blogname):
    '''
    given the url for a blog, returns a list of all the Image posts that have tags.
    '''
    api = Api(blogname)
    imgPosts = api.read(type='photo')
    return filter(lambda x: 'tags' in x, imgPosts)
        
#def getUpdated(blogname):
            
def numTags(tumblr_post):
    if 'tags' in tumblr_post:
        return len(tumblr_post['tags'])
    return 0

