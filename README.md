# 3D Model Viewer

This is a simple 3D model viewer written in Python using the PyOpenGL library. The viewer allows the user to interact with a scene of basic geometric shapes by picking, moving, scaling, and rotating them.

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Installation

Before running the program, you will need to install the following dependencies:

- NumPy
- PyOpenGL

You can install them using `pip`, the Python package manager. To install NumPy, run:

```
pip install numpy
```

To install PyOpenGL, run:

```
pip install pyopengl
```




## Usage

To run the program, execute the following command:

```
python main.py
```

This will open a window displaying the 3D scene. You can interact with the scene using the following mouse actions:

    Pick: left-click on an object to select it
    Move: left-click and drag an object to move it
    Scale: right-click and drag an object to scale it
    Rotate: left-click and drag outside an object to r


The scene contains basic geometric shapes such as spheres and cubes. You can add more shapes by modifying the node.py file. The transformation.py file contains functions to create transformation matrices such as translation and scaling matrices that can be used to transform the objects in the scene.    


`main.py`:

    This is the main Python file that launches the 3D model viewer.
    It creates an instance of the Scene class, which represents the 3D scene containing various geometric shapes.
    It uses the PyOpenGL library to render the 3D scene onto a window.
    It defines mouse callback functions for picking, moving, scaling, and rotating the shapes in the scene.

`node.py`:

    This file defines the Node class, which represents a single geometric shape in the 3D scene.
    It also defines subclasses of Node for specific shapes like spheres, cubes, and snow figures.
    Each Node has a position, rotation, and scale in 3D space, as well as methods for rendering and picking.

`scene.py`:

    This file defines the Scene class, which represents the entire 3D scene containing multiple Nodes.
    It provides methods for adding new Nodes to the scene, rendering the scene, picking objects with the mouse, and moving/scaling selected Nodes.

`transformation.py`:

    This file defines two helper functions for creating transformation matrices: translation and scaling.
    These functions return a 4x4 NumPy matrix representing a translation or scaling operation in 3D space.
