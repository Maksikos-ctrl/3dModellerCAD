from collections import defaultdict
from OpenGL.GLUT import glutGet, glutKeyboardFunc, glutMotionFunc, glutMouseFunc, glutPassiveMotionFunc, \
                        glutPostRedisplay, glutSpecialFunc
from OpenGL.GLUT import GLUT_LEFT_BUTTON, GLUT_RIGHT_BUTTON, GLUT_MIDDLE_BUTTON, \
                        GLUT_WINDOW_HEIGHT, GLUT_WINDOW_WIDTH, \
                        GLUT_DOWN, GLUT_KEY_UP, GLUT_KEY_DOWN, GLUT_KEY_LEFT, GLUT_KEY_RIGHT
import trackball



class Interaction(object):
    def __init__(self):
        """handle user interactions"""

        self.pressed = None
        
        self.window = window
        self.rotation = [0.0, 0.0, 0.0]
        self.translation = [0.0, 0.0, -5.0]

        self.translation = [0, 0, 0, 0]

        self.trackball = trackball.Trackball(theta = -25, distance = 15)

        self.mouse_loc = None

        self.callbacks = defaultdict(list)

        self.register()


    def register(self):
        """register callbacks with glut"""

        glutMouseFunc(self.handle_mouse_button)
        glutMotionFunc(self.handle_mouse_move)
        glutKeyboardFunc(self.handle_keystroke)
        glutSpecialFunc(self.handle_keystroke)
        glutSpecialFunc(self.handle_key_rotation)


    def register_callback(self, name, func):
        self.callbacks[name].append(func)



    # **kwargs allows us to pass a variable number of keyword arguments to a Python function, creates a dictionary
    # *args we use where we dunno how much args we wanna pass 
    def trigger(self, name, *args, **kwargs):  
        for func in self.callbacks[name]:  
            func(*args, **kwargs)    


    def translate(self, x, y, z):
        """apply the current interaction to the modelview matrix"""

        self.translation[0] += x
        self.translation[1] += y
        self.translation[2] += z


    def handle_mouse_button(self, button, mode, x, y):
        """ Called when the mouse button is pressed or released """

        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        # invert the y coordinate because OpenGL is inverted
        y = ySize - y;    
        self.mouse_loc = (x, y)

       
        match mode, button:
            case (GLUT_DOWN, button) if button == GLUT_RIGHT_BUTTON:
                pass
            case (GLUT_DOWN, button) if button == GLUT_LEFT_BUTTON:
                self.trigger('pick', x, y)
            case (GLUT_DOWN, 3):
                self.translate(0, 0, 1.0)
            case (GLUT_DOWN, 4):
                self.translate(0, 0, -1.0)
            case _:
                self.pressed = None
        glutPostRedisplay() 


    def handle_mouse_move(self, x, screen_y):
        """ Called when the mouse is moved """

        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        #* invert the y coordinate because OpenGL is inverted
        y = ySize - screen_y; 
       

        if self.pressed is not None:
            dx = x - self.mouse_loc[0]
            dy = y - self.mouse_loc[1]

            if self.pressed == GLUT_RIGHT_BUTTON and self.trackball is not None:
                self.trackball.drag_to(self.mouse_loc[0], self.mouse_loc[1], dx, dy)
            elif self.pressed == GLUT_LEFT_BUTTON:
                self.trigger('move', x, y)
            elif self.pressed == GLUT_MIDDLE_BUTTON:
                self.translate(dx/60.0, dy/60.0, 0)    
            else:
                pass        
            glutPostRedisplay()
        self.mouse_loc = (x, y)  

    def handle_keystroke(self, key, x, screen_y):
        """ Called when a key is pressed """

        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        # invert the y coordinate because OpenGL is inverted
        y = ySize - screen_y;  

        if key == ord('s'):
            self.trigger('place', 'sphere', x, y)
        elif key == ord('c'):
            self.trigger('place', 'cube', x, y)
        elif key == GLUT_KEY_UP:
            self.trigger('scale', up=True)
        elif key == GLUT_KEY_DOWN:
            self.trigger('scale', up=False)
        elif key == GLUT_KEY_LEFT:
            self.trigger('rotate_color', forward=True)
        elif key == GLUT_KEY_RIGHT:
            self.trigger('rotate_color', forward=False)
        glutPostRedisplay() 
        
        
    def handle_key_rotation(self, key, x, y, step):
        if key == b"x":
            self.rotation[0] += step
        elif key == b"y":
            self.rotation[1] += step
        elif key == b"z":
            self.rotation[2] += step
        glutPostRedisplay()


    




    
          
        
        



