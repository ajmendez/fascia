'''server.py -- A simple tornado server
2014.May : Mendez
'''
import os
import sys
import tornado.ioloop
import tornado.web
from datetime import datetime

HOSTNAME = 'localhost'
PORT = 5555




class MainHandler(tornado.web.RequestHandler):
    '''Handles the web requests'''
    def get(self):
        items = ['a','b']
        time = datetime.now()
        self.render('home.html', items=items, time=time)
        # self.write("Hello, world")
        # print 'client'
        sys.stdout.write('.')
        sys.stdout.flush()


def server(hostname, port):
    '''Setup the server on this port'''
    print 'Starting the Server!'
    try:
        mainpath = os.path.dirname(__file__)
        settings = dict(
            template_path = os.path.join(mainpath, "templates"),
            debug = True,
        )
        
        handlers = [
            (r"/", MainHandler),
            (r"/static/(.*)", tornado.web.StaticFileHandler, 
                              {"path": os.path.join(mainpath,'static')}),
        ]
        
        application = tornado.web.Application(handlers, **settings)
        application.listen(port)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print 'Bye!'
    except:
        raise

if __name__ == '__main__':
    server(HOSTNAME, PORT)