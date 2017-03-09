'''Graph creator'''


class Graph(object):
    '''Graph constructor'''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [width, height]
        #self.coordinates=[]

    def in_boundary(self, _id):
        '''checks if node is in grid'''
        (x, y)=_id
        return 0 <= x < self.width and 0 <= y < self.height

    def get_neighbors(self, _id):
        '''Looks for the node's neighbors'''
        (x, y)=_id
        results = [(x+1,y),(x,y-1),(x-1,y),(x,y+1)]
        if(x+y)% 2 == 0: results.reverse()
        results = filter(self.boundary,results)
        results = filter(self.passable,results)
        return results