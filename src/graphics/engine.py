from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import threading

from graphics.camera import *


class GraphicsEngine:
    def __init__(self, width, height, camera, drawingFunction, keyboardFunction):
        # Properties
        self.width = width
        self.height = height
        self.camera = camera
        self.drawingFunction = drawingFunction
        self.keyboardFunction = keyboardFunction

        print("Initialising OpenGL")
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(100, 100)

        print("Starting window")
        self.windowId = glutCreateWindow("GraphicsEngine")

        print("Configuring OpenGL")
        glClearColor(0.0, 0.0, 0.0, 0.0)

        glutDisplayFunc(self.displayFunc)
        glutIdleFunc(self.displayFunc)
        glutReshapeFunc(self.camera.reshapeFunction)
        glutKeyboardFunc(self.keyboardFunction)

        threading.Thread(target=glutMainLoop).start()

    def stop(self):
        if self.windowId is not None:
            glutDestroyWindow(self.windowId)
            print("Destroyed window " + name)

    def displayFunc(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.camera.doLookAt()
        self.drawingFunction()
        glutSwapBuffers()


class Cube:
    def draw(self):
        glEnable(GL_POINT_SMOOTH)
        glPointSize(3)
        glBegin(GL_POINTS)
        glColor3fv((1.0, 1.0, 1.0))
        glVertex3f(0.0, 0.0, 0.0)
        glVertex3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(0.0, 0.0, 1.0)
        glVertex3f(1.0, 0.0, 1.0)
        glVertex3f(0.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glEnd()


class ObjectGraphicsEngineRadialCamera(GraphicsEngine):
    def __init__(self, width, height):
        self.objects = [Cube()]
        super().__init__(
            width, height, RadialCamera(), self.drawingFunction, self.keyboardFunction
        )
        self.camera.setRadius(10)

    def drawingFunction(self):
        for obj in self.objects:
            obj.draw()

    def keyboardFunction(self, key, x, y):
        if ord(key) == 113:
            glutDestroyWindow(self.windowId)
            # self.keepOpen = False
            return
        if ord(key) == 97:
            self.camera.setHorizontalAngle(self.camera.getHorizontalAngle() - 0.1)
            return
        if ord(key) == 100:
            self.camera.setHorizontalAngle(self.camera.getHorizontalAngle() + 0.1)
            return
        if ord(key) == 115:
            self.camera.setVerticalAngle(self.camera.getVerticalAngle() - 0.1)
            return
        if ord(key) == 119:
            self.camera.setVerticalAngle(self.camera.getVerticalAngle() + 0.1)
            return
