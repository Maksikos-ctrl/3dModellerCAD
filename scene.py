import sys
import numpy
from node import Sphere, Cube, SnowFigure


class Scene(object):


    PLACE_DEPTH = 15.0


    def __init__(self):
        self.node_list = []
        # Keep track of the currently selected node.
        self.selected_node = None


    def add_node(self, node):
        self.node_list.append(node)


    def render(self):
        for node in self.node_list:
            node.render()        
        