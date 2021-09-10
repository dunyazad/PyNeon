from .NCommon import *
from .NSceneNode import *

class NSceneNodeCamera(NSceneNode):
    def __init__(self, sceneLayer, name):
        super().__init__(sceneLayer, name)
        
        self.projectionMatrix = glm.perspective(glm.radians(45), 1280/720, 0.1, 10000)
        self.viewMatrix = glm.lookAt(glm.vec3(0, 0, 0), glm.vec3(0, 0, -1), glm.vec3(0, 1, 0))

    def GetProjectionMatrix(self):
        return self.projectionMatrix

    def SetProjectionMatrix(self, projectionMatrix):
        self.projectionMatrix = projectionMatrix

    def GetViewMatrix(self):
        return self.viewMatrix

    def SetViewMatrix(self, viewMatrix):
        self.viewMatrix = viewMatrix
