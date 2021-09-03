from .NCommon import *

class NRenderer:
    def __init__(self, window):
        self.window = window

    def Render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glfw.swap_buffers(self.window.glfwWindow)
