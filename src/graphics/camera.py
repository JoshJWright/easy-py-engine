import math
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Camera:
    cameraPosition = (0.0, 0.0, 0.0)
    targetPosition = (0.0, 0.0, 0.0)
    upVector = (0.0, 1.0, 0.0)

    def getCamPos(self):
        return self.cameraPosition

    def setCamPos(self, pos: tuple):
        self.cameraPosition = pos

    def getTgtPos(self):
        return self.targetPosition

    def setTgtPos(self, pos: tuple):
        self.targetPosition = pos

    def getUpVec(self):
        return self.upVector

    def setUpVec(self, vec: tuple):
        self.upVector = vec

    def reshapeFunction(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, w / h, 1.0, 200.0)
        glMatrixMode(GL_MODELVIEW)

    def doLookAt(self):
        gluLookAt(
            self.cameraPosition[0],
            self.cameraPosition[1],
            self.cameraPosition[2],
            self.targetPosition[0],
            self.targetPosition[1],
            self.targetPosition[2],
            self.upVector[0],
            self.upVector[1],
            self.upVector[2],
        )


class RadialCamera(Camera):

    horizontalAngle = 0.0
    verticalAngle = 0.0
    radius = 0.0

    def getHorizontalAngle(self):
        return self.horizontalAngle

    def setHorizontalAngle(self, theta):
        self.horizontalAngle = theta

    def getVerticalAngle(self):
        return self.verticalAngle

    def setVerticalAngle(self, theta):
        if abs(theta) < math.pi / 2:
            self.verticalAngle = theta

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def doLookAt(self):
        rHorizontal = self.radius * math.cos(self.verticalAngle % (2 * math.pi))
        rVertical = self.radius * math.sin(self.verticalAngle % (2 * math.pi))
        self.cameraPosition = (
            self.targetPosition[0]
            + rHorizontal * math.sin(self.horizontalAngle % (2 * math.pi)),
            self.targetPosition[1] + rVertical,
            self.targetPosition[2]
            + rHorizontal * math.cos(self.horizontalAngle % (2 * math.pi)),
        )
        super().doLookAt()
