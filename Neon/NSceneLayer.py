from .NCommon import *
from .NSceneNode import *

class NSceneLayer:
    def __init__(self, scene, name):
        self.name = name
        self.scene = scene
        self.rootNode = NSceneNode(self, name)

    def CreateSceneNode(self, name, parent = None):
        sceneNode = NSceneNode(self, name)
        if parent is None:
            self.rootNode.AddChild(sceneNode)
        else:
            parent.AddChild(sceneNode)
        return sceneNode

    def GetRootNode(self):
        return self.rootNode

    def Update(self, timeDelta):
        self.rootNode.Update(timeDelta)

    def Render(self):
        self.rootNode.Render()