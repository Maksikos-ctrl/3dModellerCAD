import unittest 
from unittest.mock import MagicMock
from main import Viewer

class TestViewer(unittest.TestCase):

    def setUp(self):
        self.viewer = Viewer()


    def test_init_interface(self):
        self.viewer.init_interface()
        glutInit.assert_called_once_with()
        glutInitWindowSize.assert_called_once_with(1080, 720)
        glutCreateWindow.assert_called_once_with("3d Model Viewer")
        glutInitDisplayMode.assert_called_once_with(GLUT_RGB | GLUT_SINGLE)
        glutDisplayFunc.assert_called_once_with(self.viewer.renderer)  


    def test_init_opengl(self):
        self.viewer.init_opengl()
        glEnable.assert_called_once_with(GL_CULL_FACE)
        glCullFace.assert_called_once_with(GL_BACK)
        glEnable.assert_called_once_with(GL_DEPTH_TEST)
        glDepthFunc.assert_called_once_with(GL_LESS)
        glEnable.assert_called_once_with(GL_LIGHT0)
        glLightfv.assert_any_call(GL_LIGHT0, GL_POSITION, GLfloat_4(0, 0, 0, 1))
        glLightfv.assert_any_call(GL_LIGHT0, GL_SPOT_DIRECTION, GLfloat3(0, 0, -1))
        glColorMaterial.assert_called_once_with(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable.assert_called_once_with(GL_COLOR_MATERIAL)
        glClearColor.assert_called_once_with(0.4, 0.4, 0.4, 0)


    def test_create_sample_scane(self):
        self.viewer.create_sample_scene()
        self.assertEqual(len(self.viewer.scene.nodes), 2) 


    def test_render(self):
        #TODO mock others method calls and test the output of the func
        pass       


    #TODO write tests for other methods

if __name__ == '__main__':
    unittest.main()





    