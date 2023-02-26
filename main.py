from OpenGL.GL import glCallList, glClear, glClearColor, glColorMaterial, glCullFace, glDepthFunc, glDisable, glEnable,\
                      glFlush, glGetFloatv, glLightfv, glLoadIdentity, glMatrixMode, glMultMatrixf, glPopMatrix, \
                      glPushMatrix, glTranslated, glViewport, \
                      GL_AMBIENT_AND_DIFFUSE, GL_BACK, GL_CULL_FACE, GL_COLOR_BUFFER_BIT, GL_COLOR_MATERIAL, \
                      GL_DEPTH_BUFFER_BIT, GL_DEPTH_TEST, GL_FRONT_AND_BACK, GL_LESS, GL_LIGHT0, GL_LIGHTING, \
                      GL_MODELVIEW, GL_MODELVIEW_MATRIX, GL_POSITION, GL_PROJECTION, GL_SPOT_DIRECTION
from OpenGL.constants import GLfloat_3, GLfloat_4
from OpenGL.GLU import gluPerspective, gluUnProject
from OpenGL.GLUT import glutCreateWindow, glutDisplayFunc, glutGet, glutInit, glutInitDisplayMode, \
                        glutInitWindowSize, glutMainLoop, \
                        GLUT_SINGLE, GLUT_RGB, GLUT_WINDOW_HEIGHT, GLUT_WINDOW_WIDTH

import numpy
from numpy.linalg import norm, inv



from scene import Scene
from primitive import init_primitives, G_OBJ_PLANE




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
        # determines how long our object is related relatively to the camera
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
        glEnable(GL_LIGHTING)
    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
       

        # here i will create modelview matrix
        glMatrixMode(GL_MODELVIEW_MATRIX)
        glPushMatrix() 
        glLoadIdentity()
        loc_of_camera = self.interaction.translation 

        # move camera to location
        glTranslated(loc_of_camera [0], loc_of_camera[1], loc_of_camera[2])
        # rotation matrix
        glMultMatrixf(self.interaction.rotation) 

        # store the inverse of modelview matrix

        currModelView = numpy.array(glGetFloatv(GL_MODELVIEW_MATRIX))
        self.modelView = numpy.transpose(currModelView)
        self.inverseModelView = inv(numpy.transpose(currModelView))


        # render the scene, which will call all objects from render function

        self.scene.render()
        


        # draw the grid-scene

        glDisable(GL_LIGHTING)
        glCallList(G_OBJ_PLANE)
        glPopMatrix()

 
        # flush the buffer, cuz it allows the scene can be drawn
        glFlush()


    def init_view(self):
        """Init projection matrix"""

        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        aspect_ratio = float(xSize) / float(ySize)

        # load the projection matrix
        glMatrixMode(GL_PROJECTION)
        # we need identity matrix for projection matrix, identity matrix is a matrix with 1 on the diagonal and 0 everywhere else
        glLoadIdentity()

        glViewport(0, 0, xSize, ySize)
        gluPerspective(70, aspect_ratio, 0.1, 1000.0)
        glTranslated(0, 0, -15)



    




















        
       



    def main_loop(self):
        glutMainLoop()

        
if __name__ == "__main__": 
    viewer = Viewer()
    viewer.main_loop()
        







