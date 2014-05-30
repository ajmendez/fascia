'''reddit.py -- Get gifs from reddit
May 2014: Mendez
'''

import os
import sys
import praw
import json
import requests
from pprint import pprint
from pymendez.auth import auth


from pysurvey import util
util.setup_stop()

USERNAME,PASSWORD = auth('reddit', ('username','password'))
MAINDIR = os.path.dirname(__file__)
STORAGE = os.path.join(MAINDIR, 'cache', 'reddit.json')
IMAGES  = os.path.join(MAINDIR, 'static', 'images', 'reddit')
SUBREDDITS = ('cinemagraphs', 'perfectloops')


class Reddit(object):
    """Reddit data parser"""
    def __init__(self, username=USERNAME, password=PASSWORD):
        self.r = praw.Reddit('fascia dashboard')
        self.r.login(username, password)
    
    def load(self, filename=STORAGE):
        '''Load the data.'''
        try:
            self.data = json.load(open(filename, 'r'))
        except IOError:
            self.data = {}
    
    def save(self, filename=STORAGE):
        '''Save the data'''
        json.dump(self.data, open(filename, 'w'), indent=2, sort_keys=True)
    
    def update(self, subreddits=SUBREDDITS):
        '''update the self.data archive of posts'''
        for subreddit in subreddits:
            self.updateposts(subreddit)
    
    def list(self):
        '''List the current posts'''
        for value in self.data.values():
            self.saveimage(value)
            print ' * %(name)10s \n   > %(title)s \n   > %(url)s'%value
        print 'items: ', len(self.data)
    
    def display(self):
        '''return the image -- and state it has been used'''
        return self.data['26tths']
    
    def updateposts(self, name):
        '''get the top posts from the week'''
        sub = self.r.get_subreddit(name)
        for post in sub.get_top_from_week():
            if self.imagefilter(post):
                tmp = self.parsepost(post)
                self.saveimage(tmp)
                self.data[tmp['name']] = tmp
            
            sys.stdout.write('.')
            sys.stdout.flush()
        print
            
    
    def imagefilter(self, post):
        '''Check if this is a image post.  Right now filter to be image post'''
        exts = ['.png','.jpg','.gif']
        return any([post.url.endswith(ext) for ext in exts])
    
    def saveimage(self, post):
        ext = os.path.splitext(post['url'])[1]
        filename = os.path.join(IMAGES, post['name']+ext)
        post['filename'] = filename
        if os.path.exists(filename):
            return
        r = requests.get(post['url'])
        open(filename, 'w').write(r.content)
        post['filename'] = filename
        
    def parsepost(self, post):
        '''get the specific information for the post'''
        return dict(url = post.url,
                    name = post.id, # possible should use name ?
                    title = post.title,)



if __name__ == '__main__':
    r = Reddit()
    r.load()
    # r.update()
    r.list()
    r.save()