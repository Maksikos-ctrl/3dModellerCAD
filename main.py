import os
import numpy
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Viewer(object):
    def __init__(self):
        self.init_interface()
        self.init_opengl()
        self.init_scene()
        self.init_interaction()
        init_primitives()

    def init_interface(self):
        """init window and register the render function"""
        glutInit()
        glutInitWindowSize(1080, 720)
        glutCreateWindow("3d Model Viewer");
        glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
        glutDisplayFunc(self.renderer) 


    def init_opengl(self):
        """initialization of OpenGL for rendering scene"""
        self.inverseModelView = numpy.identity(4)
        self.modelView = numpy.identity(4)

        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        glEnable(GL_LIGHT0)
        # light position
        glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(0, 0, 0, 1))
        # light direction
        glLightfv(GL_LIGHT0, GL_DIRECTION, GLfloat3(0, 0, -1))

        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)
        # clear color for background 
        glClearColor(0.4, 0.4, 0.4, 0)  


    def init_scene(self):
        """init scene object and init scene"""

        self.scene = Scene()
        self.create_sample_scene()


    def create_sample_scene(self):
        cube_node = Cube()
        cube_node.translate(2, 0, 2)
        cube_node.color_index = 2
        self.scene.add_node(cube_node)

        sphere_node = Sphere()
        sphere_node.translate(-2, 0, 2)
        sphere_node.color_index = 3
        self.scene.add_node(sphere_node)


    def init_interaction(self):
        """init user interaction and callback"""  

        self.interaction = Interaction()
        # register pick callback
        self.interaction.register_callback('pick', self.pick)
        self.interaction.register_callback('move', self.move)
        self.interaction.register_callback('place', self.place)
        self.interaction.register_callback('rotate_color', self.rotate_color)
        self.interaction.register_callback('scale', self.scale)        

   
    def render(self):
        """The render passes for the scene"""
        self.init_view()

        



    def main_loop(self):
        glutMainLoop()

        
if __name__ == "__main__":
    viewer = Viewer()
    viewer.main_loop()
        







