import unittest
from unittest.mock import MagicMock, patch
from OpenGL.GL import *
from OpenGL.GLU import *
from main import Viewer
from scene import Scene, Cube, Sphere, SnowFigure, SnowFigure1,  Node
import numpy



class TestScene(unittest.TestCase):

    def setUp(self):
        self.scene = Scene()
        self.cube = Cube()
        self.sphere = Sphere()
        self.snow_figure = SnowFigure()
        self.snow_figure = SnowFigure1()

    def test_add_node(self):
        self.assertEqual(len(self.scene.node_list), 0)
        self.scene.add_node(self.cube)
        self.assertEqual(len(self.scene.node_list), 1)
        self.assertEqual(self.scene.node_list[0], self.cube)

    def test_render(self):
        with patch.object(Node, 'render', return_value=None) as mock_render:
            self.scene.node_list = [self.cube, self.sphere, self.snow_figure]
            self.scene.render()
            self.assertEqual(mock_render.call_count, 3)
            
    def test_pick_no_hit(self):
        
        self.assertIsNone(self.scene.selected_node)


    def test_pick_hit(self):
        start = numpy.array([0, 0, 0])
        direction = numpy.array([0, 0, -1])
        mat = numpy.identity(4)
        self.cube.pick = MagicMock(return_value=(True, 10))
        self.sphere.pick = MagicMock(return_value=(False, 0))
        self.snow_figure.pick = MagicMock(return_value=(True, 5))
        self.scene.node_list = [self.cube, self.sphere, self.snow_figure]
        self.assertIsNone(self.scene.selected_node)
        self.scene.pick(start, direction, mat)
        self.assertEqual(self.scene.selected_node, self.snow_figure)
        self.snow_figure.pick.assert_called_once_with(start, direction, mat)
        self.cube.pick.assert_called_once_with(start, direction, mat)
        self.sphere.pick.assert_called_once_with(start, direction, mat)

   


if __name__ == '__main__':
    unittest.main()





    