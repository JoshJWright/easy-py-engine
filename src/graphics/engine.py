from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import threading

class GraphicsEngine:

    def __init__(self, width=500, height=500, camera, drawingFunction, keyboardFunction):
        # Properties
        self.width = width
        self.height = height
        self.camera = camera
        self.drawingFunction = drawingFunction
        self.keyboardFunction = keyboardFunction
        
        # Initialise OpenGL
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(100,100)

        # Configure OpenGL
        glClearColor(0.0, 0.0, 0.0, 0.0)

        # Assign callbacks
        glutDisplayFunc(self.drawingFunction)
        glutIdleFunc(self.drawingFunction)
        glutReshapeFunc(self.camera.reshapeFunction)
        glutKeyboardFunc(self.keyboardFunction)

    def start(name="Graphics Engine"):
        self.windowId = glutCreateWindow(name)
        threading.Thread(target=glutMainLoop).start()
    
    def stop():
        glutDestroyWindow(self.windowId)
        

