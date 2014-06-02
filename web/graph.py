'''graph.py -- make some nice graphs
June 2014 : Mendez
'''
import pylab


class Graph(object):
    def __init__(self, width=800, height=500):
        self.width = width
        self.height = height
    
    def update(self):
        '''grab the data'''
    
    def display(self):
        '''Make the plot'''
    
    def show(self):
        '''show the plot'''
        self.display()
        pylab.show()




if __name__ == '__main__':
    g = Graph()
    g.update()
    # g.display()
    g.show()