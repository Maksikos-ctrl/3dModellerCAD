import unittest
from unittest.mock import MagicMock, patch
from OpenGL.GL import *
from OpenGL.GLU import *
from main import Viewer
from scene import Scene

class TestViewer(unittest.TestCase):

    def setUp(self):
        self.viewer = Viewer()


    def test_init_interface(self):
        with patch('OpenGL.GLUT.glutInit') as glutInit:
            self.viewer.init_interface()
            glutInit.assert_called_once_with()


    def test_init_opengl(self):
        with patch('OpenGL.GL.glEnable') as glEnable, \
                patch('OpenGL.GL.glClearColor') as glClearColor, \
                patch('OpenGL.GL.glMatrixMode') as glMatrixMode, \
                patch('OpenGL.GL.glLoadIdentity') as glLoadIdentity, \
                patch('OpenGL.GLU.gluOrtho2D') as gluOrtho2D:
            self.viewer.init_opengl()
            glEnable.assert_called_once_with(GL_CULL_FACE)
            glClearColor.assert_called_once_with(0.0, 0.0, 0.0, 0.0)
            glMatrixMode.assert_called_once_with(GL_PROJECTION)
            glLoadIdentity.assert_called_once_with()
            gluOrtho2D.assert_called_once_with(0, 640, 0, 480)


    def test_create_sample_scene(self):
        self.viewer.scene = Scene()
        self.viewer.create_sample_scene()
        self.assertEqual(len(self.viewer.scene.node_list), 3)

     
   

if __name__ == '__main__':
    unittest.main()





    