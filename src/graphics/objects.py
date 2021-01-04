from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


class SceneObject:
    position = (0.0, 0.0, 0.0)

    def drawAtPos(self):
        glPushMatrix()
        glTranslatef(self.position[0], self.position[1], self.position[2])
        # glTranslatef(position[0], position[1], position[2])
        self.draw()
        glPopMatrix()

    def draw(self):
        pass


class Vertex(SceneObject):
    def __init__(
        self,
        point: tuple,
        size: float = 3.0,
        color: tuple = (1.0, 1.0, 1.0),
    ):
        self.point = point
        self.size = size
        self.color = color

    def draw(self):
        glEnable(GL_POINT_SMOOTH)
        glPointSize(self.size)
        glBegin(GL_POINTS)
        glColor3fv(self.color)
        glVertex3fv(self.point)
        glEnd()


class Edge(SceneObject):
    def __init__(
        self,
        start: Vertex,
        end: Vertex,
        width: float = 1.0,
        color: tuple = (1.0, 1.0, 1.0),
    ):
        self.start = start
        self.end = end
        self.width = width
        self.color = color

    def draw(self):
        glEnable(GL_LINE_SMOOTH)
        glLineWidth(self.width)
        glBegin(GL_LINES)
        glColor3fv(self.color)
        glVertex3fv(self.start.point)
        glVertex3fv(self.end.point)
        glEnd()


class Triangle(SceneObject):
    def __init__(self, a: Vertex, b: Vertex, c: Vertex, color: tuple = (1.0, 1.0, 1.0)):
        self.a = a
        self.b = b
        self.c = c
        self.color = color

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3fv(self.color)
        glVertex3fv(self.a.point)
        glVertex3fv(self.b.point)
        glVertex3fv(self.c.point)
        glEnd()


class Quad(SceneObject):
    def __init__(
        self, a: Vertex, b: Vertex, c: Vertex, d: Vertex, color: tuple = (1.0, 1.0, 1.0)
    ):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.color = color

    def draw(self):
        glBegin(GL_QUADS)
        glColor3fv(self.color)
        glVertex3fv(self.a.point)
        glVertex3fv(self.b.point)
        glVertex3fv(self.c.point)
        glVertex3fv(self.d.point)
        glEnd()


class Polygon(SceneObject):
    def __init__(self, vertices: list, color: tuple):
        self.vertices = vertices
        self.color = color

    def draw(self):
        glBegin(GL_POLYGON)
        glColor3fv(self.color)
        for v in self.vertices:
            glVertex3fv(v)
        glEnd()


class TestCube(SceneObject):
    def draw(self):
        a = Vertex((1, 1, 1))
        b = Vertex((1, -1, 1))
        c = Vertex((-1, -1, 1))
        d = Vertex((-1, 1, 1))
        e = Vertex((1, 1, -1))
        f = Vertex((1, -1, -1))
        g = Vertex((-1, -1, -1))
        h = Vertex((-1, 1, -1))
        Quad(a, b, c, d, (0.9, 0.0, 0.0)).draw()
        Quad(e, f, g, h, (0.0, 0.45, 0.45)).draw()
        Quad(a, b, f, e, (0.0, 0.9, 0.0)).draw()
        Quad(c, d, h, g, (0.45, 0.0, 0.45)).draw()
        Quad(a, d, h, e, (0.0, 0.0, 0.9)).draw()
        Quad(b, c, g, f, (0.45, 0.45, 0.0)).draw()
