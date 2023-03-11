import unittest 
from unittest.mock import MagicMock
from main import Viewer
from OpenGL.GL import GL_AMBIENT_AND_DIFFUSE, GL_BACK, GL_CULL_FACE, GL_COLOR_MATERIAL, \
                      GL_DEPTH_TEST, GL_FRONT_AND_BACK, GL_LESS, GL_LIGHT0, \
                      GL_POSITION, GL_SPOT_DIRECTION

from OpenGL.GLUT import GLUT_SINGLE, GLUT_RGB

class TestViewer(unittest.TestCase):

    def setUp(self):
        self.viewer = Viewer()


    def test_init_interface(self):
        # Mock the functions that are called inside init_interface method
        glutInit = MagicMock()
        glutInitWindowSize = MagicMock()
        glutCreateWindow = MagicMock()
        glutInitDisplayMode = MagicMock()
        glutDisplayFunc = MagicMock()


        # Call the init_interface method
        self.viewer.init_interface()

        # Assert that the mocked functions were called with the expected arguments
        glutInit.assert_called_once_with()
        glutInitWindowSize.assert_called_once_with(1080, 720)
        glutCreateWindow.assert_called_once_with("3d Model Viewer")
        glutInitDisplayMode.assert_called_once_with(GLUT_RGB | GLUT_SINGLE)
        glutDisplayFunc.assert_called_once_with(self.viewer.renderer)



    def test_init_opengl(self):
        # Mock the OpenGL functions that are called inside init_opengl method
        glEnable = MagicMock()
        glCullFace = MagicMock()
        glDepthFunc = MagicMock()
        glLightfv = MagicMock()
        glColorMaterial = MagicMock()
        glClearColor = MagicMock()

        # Call the init_opengl method
        self.viewer.init_opengl()

        # Assert that the mocked OpenGL functions were called with the expected arguments
        glEnable.assert_any_call(GL_CULL_FACE)
        glCullFace.assert_called_once_with(GL_BACK)
        glEnable.assert_any_call(GL_DEPTH_TEST)
        glDepthFunc.assert_called_once_with(GL_LESS)
        glEnable.assert_any_call(GL_LIGHT0)
        glLightfv.assert_any_call(GL_LIGHT0, GL_POSITION, [0, 0, 0, 1])
        glLightfv.assert_any_call(GL_LIGHT0, GL_SPOT_DIRECTION, [0, 0, -1])
        glColorMaterial.assert_called_once_with(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable.assert_called_once_with(GL_COLOR_MATERIAL)
        glClearColor.assert_called_once_with(0.4, 0.4, 0.4, 0)


    def test_create_sample_scane(self):
       # Call the create_sample_scene method
        self.viewer.create_sample_scene()

        # Assert that the scene has two nodes
        self.assertEqual(len(self.viewer.scene.nodes), 2)

     
   

if __name__ == '__main__':
    unittest.main()





    