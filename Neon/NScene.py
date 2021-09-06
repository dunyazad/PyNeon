from .NCommon import *
from .NSceneLayer import *

class NScene:
    def __init__(self, name):
        self.name = name
        self.sceneLayers = {}

    def CreateSceneLayer(self, name):
        if name not in self.sceneLayers.items():
            self.sceneLayers[name] = NSceneLayer(self, name)

        return self.sceneLayers[name]

    def Update(self, timeDelta):
        for name, sceneLayer in self.sceneLayers.items():
            sceneLayer.Update(timeDelta)

    def Render(self):
        for name, sceneLayer in self.sceneLayers.items():
            sceneLayer.Render()
