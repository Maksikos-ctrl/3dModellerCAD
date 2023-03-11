import sys
import numpy
from node import Sphere, Cube, SnowFigure



class Scene(object):

    # the default depth from the camera to place an object at
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


    def pick(self, start, dir, mat):
        """ 
        Execute selection.
            
        start, direction describe a Ray. 
        mat is the inverse of the current modelview matrix for the scene.
        """      

        if self.selected_node is not None:
            self.selected_node.select(False)
            self.selected_node = None


        # Keep track of the currently selected
        mindist = sys.maxint  
        closest_node = None

        for node in self.node_list:
            hit, dist = node.pick(start, dir, mat)
            if hit and dist < mindist:
                mindist, closest_node = dist, node  
            

        if closest_node is not None:
            closest_node.select()
            closest_node.depth = mindist
            closest_node.selected_loc = start + dir * mindist
            self.selected_node = closest_node 

    

    def scale_selected(self, up):
        """ Scale the current selection """
        if self.selected_node is None: return
        self.selected_node.scale(up)


    def scale(scale):
        s = numpy.identity(4)
        s[0, 0] = scale[0]
        s[1, 1] = scale[1]
        s[2, 2] = scale[2]
        s[3, 3] = 1
        return s



    def move_selected(self, start, dir, inv_modelview):
        """ 
        Move the selected node, if there is one.
            
        Consume: 
        start, direction describes the Ray to move to
        mat i  
        """

        if self.selected_node is None: return


        # Find the current depth and location of the selected node

        node = self.selected_node
        depth = node.depth
        oldLoc = node.selected_loc


        # The new loc of the node is the same depth along the new ray
        newLoc = (start + dir * depth)


        # transform the translation with the modelview matrix

        trans = newLoc - oldLoc
        pre_trans = numpy.array([trans[0], trans[1], trans[2], 0])
        trans = inv_modelview.dot(pre_trans)


        # translate the node and track its location
        node.translate(trans[0], trans[1], trans[2])
        node.selected_loc = newLoc
    
            






    