from .NCommon import *
from .NWindow import *

from .Scene import *
from .Graphics import *

class Neon:
    def __init__(self):
        self.windows = []

        glfw.init()

    def __del__(self):
        glfw.terminate()

    def CreateWindow(self, windowWidth, windowHeight):
        window = NWindow(windowWidth, windowHeight)
        self.windows.append(window)
        return window