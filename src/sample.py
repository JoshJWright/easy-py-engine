from graphics.engine import *
from graphics.objects import *
from time import sleep
import random

ge = ObjectGraphicsEngineRadialCamera(
    500,
    500,
)

ge.addSceneObject(TestCube())
a = TestCube()
ge.addSceneObject(a)

while True:
    sleep(0.5)
    a.position = (1, 1, 1)
