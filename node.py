import random
from OpenGL.GL import glCallList, glColor3f, glMaterialfv, glMultMatrixf, glPopMatrix, glPushMatrix, \
                      GL_EMISSION, GL_FRONT
import numpy

from primitive import G_OBJ_CUBE, G_OBJ_SPHERE
from aabb import AABB
from transformation import scaling, translation
import color




## axis-aligned bounding box aabb

class Node(object):


    def __init__(self):
        self.color_indx = random.randint(color.MIN_COLOR, color.MAX_COLOR)
        ## axis-aligned bounding box aabb - rectangular parallelepiped whose faces are each perpendicular to one of the basis vectors. Such bounding boxes arise frequently in spatial subdivision problems, such as in ray tracing or collision detection
        self.aabb = AABB([0.0, 0.0, 0.0], [0.5, 0.5, 0.5])
        self.translation_matrix = numpy.identity(4);
        self.selected = False

    def render(self):
        """render items to the scree"""

        glPushMatrix()
        glMultMatrixf(numpy.identity(self.translation_matrix))
        glMultMatrixf(numpy.identity(self.scaling_matrix))
        curr_color = color.COLORS[self.color_indx]
        glColor3f(curr_color[0], curr_color[1], curr_color[2])

        


        if self.selected:
            glMaterialfv(GL_FRONT, GL_EMISSION, [0.5, 0.5, 0.5])

        self.render_self()


        if self.selected:
            glMaterialfv(GL_FRONT, GL_EMISSION, [0.0, 0.0, 0.0])
        glPopMatrix()

    def render_self(self):
        # raise == throw
        raise NotImplementedError("Unfornunately, the abstract node class doesn't define a render_self method.  You should use a subclass of Node instead.")
    

    def pick(self, start, dir, mat):
        """ 
        Return whether or not the ray hits the object

        Consume:  
        start, direction form the ray to check
        mat
        """

        newmat = numpy.dot(
            numpy.dot(mat, self.translation_matrix), 
            numpy.linalg.inv(self.scaling_matrix)
        )
        results = self.aabb.ray_hit(start, dir, newmat)
        return results


    def select(self, select=None):
        """ Toggles or sets selected state """

        if select is not None:
            self.selected = select
        else:
            self.selected = not self.selected    


    def rotate_color(self, forwards):
        self.color_indx += 1 if  forwards else -1
        if self.color_indx > color.MAX_COLOR:
            self.color_indx = color.MIN_COLOR
        if self.color_indx < color.MIN_COLOR:
            self.color_indx = color.MAX_COLOR  



class Primitive(Node):
    def __init__(self):
        super(Primitive, self).__init__()
        self.call_list = None

    def render_self(self):
        glCallList(self.call_list)




class Sphere(Primitive):
    """pritime of the sphere"""     

    def __init__(self):
        super(Sphere, self).__init__()
        self.call_list = G_OBJ_SPHERE

class Cube(Primitive):
    """cube of the cube"""

    def __init__(self):
        # super method takes all method from Class
        super(Cube, self).__init__()
        self.call_list = G_OBJ_CUBE


class HierarchicalNode(Node):
    def __init___(self):
        super(HierarchicalNode, self).__init()
        self.child_nodes = []


    def render_self(self):
        for child in self.child_nodes:
            child.render() 


class SnowFigure(HierarchicalNode):
    def __init__(self):
        super(SnowFigure, self).__init__() # super method takes all method from Class HierarchicalNode and Node 
        self.child_nodes = [Sphere(), Sphere(), Sphere()]       
        self.child_nodes[0].translate(0, -0.6, 0)
        self.child_nodes[1].translate(0, -0.6, 0)
        self.child_nodes[1].scaling_matrix = numpy.dot(self.scaling_matrix, scaling([0.8, 0.8, 0.8]))
        self.child_nodes[2].translate(0, 0.75, 0)
        self.child_nodes[2].scaling_matrix = numpy.dot(self.scaling_matrix, scaling([0.7, 0.7, 0.7]))
        for child_node in self.child_nodes:
            child_node.color_indx = self.MIN_COLOR

        self.aabb = AABB([0.0, 0.0, 0.0], [0.5, 1.1, 0.5])    




        