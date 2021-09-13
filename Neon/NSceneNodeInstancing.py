from .NCommon import *
from .NRenderer import *
from .NSceneNode import *

class NSceneNodeInstancing(NSceneNode):
    def __init__(self, sceneLayer, name):
        super().__init__(sceneLayer, name)
        self.instanceTransformsDirty = True
        self.instanceTransforms = []

    def AddTransform(self, transform):
        self.instanceTransforms.append(transform)
        self.instanceTransformsDirty = True

    def Update(self, timeDelta):
        super().Update(timeDelta)

        if self.instanceTransformsDirty == True:
            for material, geometry in self.renderDatas:
                geometry.vertexArrayObject.Bind()
                geometry.SetInstanceTransforms(self.instanceTransforms)
                geometry.vertexArrayObject.Unbind()
            instanceTransformsDirty = False

    def Render(self, renderer):
        for material, geometry in self.renderDatas:
            geometry.DrawInstanced(
                material,
                self.sceneLayer.GetCameraNode().GetProjectionMatrix(),
                self.sceneLayer.GetCameraNode().GetViewMatrix(),
                self.absoluteTransform)

        for child in self.children:
            child.Render(renderer)



