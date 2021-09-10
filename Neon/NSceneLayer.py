from .NCommon import *
from .NSceneNode import *
from .NSceneNodeCamera import *
from .NSceneNodeInstancing import *

class NSceneLayer:
    def __init__(self, scene, name):
        self.name = name
        self.scene = scene
        self.rootNode = NSceneNode(self, "RootNode")
        self.cameraNode = NSceneNodeCamera(self, "CameraNode")

    def CreateSceneNode(self, name, parent = None):
        sceneNode = NSceneNode(self, name)
        if parent is None:
            self.rootNode.AddChild(sceneNode)
        else:
            parent.AddChild(sceneNode)
        return sceneNode

    def CreateSceneNodeInstancing(self, name, parent = None):
        sceneNode = NSceneNodeInstancing(self, name)
        if parent is None:
            self.rootNode.AddChild(sceneNode)
        else:
            parent.AddChild(sceneNode)
        return sceneNode

    def CreateSceneNodeCamera(self, name, parent = None):
        sceneNode = NSceneNodeCamera(self, name)
        if parent is None:
            self.rootNode.AddChild(sceneNode)
        else:
            parent.AddChild(sceneNode)
        return sceneNode

    def GetRootNode(self):
        return self.rootNode

    def GetCameraNode(self):
        return self.cameraNode

    def Update(self, timeDelta):
        self.rootNode.Update(timeDelta)

    def Render(self, renderer):
        self.rootNode.Render(renderer)