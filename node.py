import random
from OpenGL.GL import glCallList, glColor3f, glMaterialfv, glMultMatrixf, glPopMatrix, glPushMatrix, \
                      GL_EMISSION, GL_FRONT
import numpy


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

        # i wanna combine to if self.selcted in one loops, help me to implement it


        if self.selected:
            glMaterialfv(GL_FRONT, GL_EMISSION, [0.5, 0.5, 0.5])

        self.render_self()


        if self.selected:
            glMaterialfv(GL_FRONT, GL_EMISSION, [0.0, 0.0, 0.0])
        glPopMatrix()




    def render_self(self):
        # raise == throw
        raise NotImplementedError("Unfornunately, the abstract node class doesn't define a render_self method.  You should use a subclass of Node instead.")


class Primitive(Node):
    """pritime of the sphere"""     

    def __init__(self):
        super(Sphere, self).__init__()
        self.call_list = G_OBJ_SPHERE

class Cube(Primitive):
    """cube of the cube"""

    def __init__(self):
        super(Cube, self).__init__()
        self.call_list = G_OBJ_CUBE
        