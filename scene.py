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


    def pick(self, start, direction, mat):
        """ Execute selection.
            Consume: start, direction describing a Ray
                     mat              is the inverse of the current modelview matrix for the scene """
        if self.selected_node is not None:
            self.selected_node.select(False)
            self.selected_node = None

        # Keep track of the closest hit.
        mindist = sys.maxsize
        closest_node = None
        for node in self.node_list:
            hit, distance = node.pick(start, direction, mat)
            if hit and distance < mindist:
                mindist, closest_node = distance, node

        # If we hit something, keep track of it.
        if closest_node is not None:
            closest_node.select()
            closest_node.depth = mindist
            closest_node.selected_loc = start + direction * mindist
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
    
    
    def place(self, shape, start, direction, inv_modelview):
        """ Place a new node.
            Consume:  shape             the shape to add
                        start, direction  describes the Ray to move to
                        inv_modelview     is the inverse modelview matrix for the scene """
        new_node = None
        if shape == 'sphere': new_node = Sphere()
        elif shape == 'cube': new_node = Cube()
        elif shape == 'figure': new_node = SnowFigure()

        self.add_node(new_node)

        # place the node at the cursor in camera-space
        translation = (start + direction * self.PLACE_DEPTH)

        # convert the translation to world-space
        pre_tran = numpy.array([translation[0], translation[1], translation[2], 1])
        translation = inv_modelview.dot(pre_tran)

        new_node.translate(translation[0], translation[1], translation[2])

    def rotate_selected_color(self, forwards):
        """ Rotate the color of the currently selected node """
        if self.selected_node is None: return
        self.selected_node.rotate_color(forwards)

    def scale_selected(self, up):
        """ Scale the current selection """
        if self.selected_node is None: return
        self.selected_node.scale(up)
    
            






    