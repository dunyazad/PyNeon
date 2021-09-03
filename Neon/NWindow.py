from .NCommon import *
from .Graphics import *

class NWindow:
    def __init__(self, windowWidth = 800, windowHeight = 600):
        self.onFrameEventHandlers = []

        self.glfwWindow = glfw.create_window(windowWidth, windowHeight, "Neon window", None, None)
    
        glfw.window_hint(glfw.SAMPLES, 4)
        glfw.make_context_current(self.glfwWindow)
        glfw.swap_interval(0)

        self.renderer = NRenderer(self)

    def Run(self):
        glClearColor(0.3, 0.5, 0.7, 1.0)
 
        now = time.time_ns()
        lastTime = time.time_ns()

        while not glfw.window_should_close(self.glfwWindow):
            glfw.poll_events()
 
            now = time.time_ns()
            timeDelta = now - lastTime
            lastTime = now

            self.renderer.Render()

            for handler in self.onFrameEventHandlers:
                handler(self, timeDelta)
    
    def SetOnFrameEventHandler(self, handler):
        self.onFrameEventHandlers.append(handler)
