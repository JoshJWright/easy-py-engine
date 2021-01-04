from graphics.engine import *
from graphics.objects import *
from time import sleep
import random

ge = ObjectGraphicsEngineRadialCamera(
    500,
    500,
)

ge.addSceneObject(TestCube())