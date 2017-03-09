'''Node creator'''


class Node:
    def __init__(self,id,val):
        self.id = id
        self.val = val
    
    def get_node(self, id, val):
        return self.id, ",", self.val
