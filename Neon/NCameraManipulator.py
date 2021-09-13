from .NCommon import *

class NCameraManipulator():
    def __init__(self, camera):
        self.camera = camera

class NCameraManipulatorFPS():
    def __init__(self, camera):
        self.camera = camera
        self.eyePosition = glm.vec3(0, 0, 0)
        self.targetPosition = glm.vec3(0, 0, -1)
        self.speed = 0.1
        self.leftButtonDown = False
        self.rightButtonDown = False
        self.angleH = 0
        self.angleV = 0
        self.lastXPos = None
        self.lastYPos = None

    def SetEyePosition(self, eyePosition):
        self.eyePosition = eyePosition
        view = glm.lookAt(self.eyePosition, self.targetPosition, glm.vec3(0, 1, 0))

    def SetTargetPosition(self, targetPosition):
        self.targetPosition = targetPosition
        view = glm.lookAt(self.eyePosition, self.targetPosition, glm.vec3(0, 1, 0))

    def OnKeyboardEvent(self, key):
        view = self.camera.GetViewMatrix()
        right = glm.vec3(glm.row(view, 0))
        up = glm.vec3(glm.row(view, 1))
        forward = -glm.vec3(glm.row(view, 2))

        if key == glfw.KEY_W:
            self.eyePosition += forward * self.speed
            self.targetPosition += forward * self.speed
        elif key == glfw.KEY_A:
            self.eyePosition -= right * self.speed
            self.targetPosition -= right * self.speed
        elif key == glfw.KEY_S:
            self.eyePosition -= forward * self.speed
            self.targetPosition -= forward * self.speed
        elif key == glfw.KEY_D:
            self.eyePosition += right * self.speed
            self.targetPosition += right * self.speed
        elif key == glfw.KEY_Q:
            self.eyePosition -= up * self.speed
            self.targetPosition -= up * self.speed
        elif key == glfw.KEY_E:
            # self.eyePosition += up * self.speed
            # self.targetPosition += up * self.speed
            self.eyePosition += glm.vec3(0, 1, 0) * self.speed
            self.targetPosition += glm.vec3(0, 1, 0) * self.speed
        elif key == glfw.KEY_LEFT_SHIFT or key == glfw.KEY_RIGHT_SHIFT:
            self.speed = 1
        
        view = glm.lookAt(self.eyePosition, self.targetPosition, glm.vec3(0, 1, 0))

        self.camera.SetViewMatrix(view)

    def OnMouseButtonEvent(self, button, action, mods):
        if button == glfw.MOUSE_BUTTON_LEFT:
            if action == glfw.PRESS:
                self.leftButtonDown = True
            elif action == glfw.RELEASE:
                self.leftButtonDown = False

        if button == glfw.MOUSE_BUTTON_RIGHT:
            if action == glfw.PRESS:
                self.rightButtonDown = True
            elif action == glfw.RELEASE:
                self.rightButtonDown = False     

    def OnMousePositionEvent(self, xPos, yPos):
        if self.lastXPos is not None and self.lastYPos is not None:
            dx = xPos - self.lastXPos
            dy = yPos - self.lastYPos
            self.lastXPos = xPos
            self.lastYPos = yPos
            
            self.angleH -= dx
            self.angleV -= dy

            view = self.camera.GetViewMatrix()

            rh = glm.angleAxis(glm.radians(self.angleH) * 0.1, glm.vec3(0, 1, 0))
            rv = glm.angleAxis(glm.radians(self.angleV) * 0.1, glm.vec3(1, 0, 0))

            self.targetPosition = self.eyePosition + rh * rv * glm.vec3(0, 0, -1)

            view = glm.lookAt(self.eyePosition, self.targetPosition, glm.vec3(0, 1, 0))

            self.camera.SetViewMatrix(view)
        else:
            self.lastXPos = xPos
            self.lastYPos = yPos