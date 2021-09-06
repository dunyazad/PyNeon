from .NCommon import *

class NSceneNode():
    def __init__(self, sceneLayer, name):
        self.sceneLayer = sceneLayer
        self.name = name
        self.renderDatas = []
        self.parent = None
        self.children = []
        self.localTransform = None
        self.absoluteTransform = None

    def GetName(self):
        return self.name

    def GetChild(self, name):
        for child in self.children:
            if child.GetName() == name:
                return child
        return None

    def AddChild(self, child):
        if child in self.children:
            return

        if child.parent is not None:
            child.parent.children.remove(child)
        
        child.parent = self
        self.children.append(child)

    def RemoveChild(self, child):
        if child not in self.children:
            return
        
        child.parent = self.sceneLayer.GetRootNode()
        self.sceneLayer.GetRootNode().children.append(child)
        self.children.remove(child)

    def AddRenderData(self, material, geometry):
        self.renderDatas.append((material, geometry))

    def GetLocalTransform(self):
        return self.localTransform

    def SetLocalTransform(self, m):
        self.localTransform = m

    def Update(self, timeDelta):
        self.absoluteTransform = self.localTransform

        for child in self.children:
            child.Update(timeDelta)

    def Render(self):
        for material, geometry in self.renderDatas:
            geometry.Draw(
                material,
                self.sceneLayer.GetCameraNode().GetProjectionMatrix(),
                self.sceneLayer.GetCameraNode().GetViewMatrix(),
                self.absoluteTransform)

        for child in self.children:
            child.Render()
