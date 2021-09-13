from .NCommon import *
from .NMaterial import *
from .NGeometry import *

class NRenderer():
    def __init__(self):
        self.renderDatas = {}

    def SetRenderData(self, material, geometry, projection, view, model):
        if (material, geometry) not in self.renderDatas:
            self.renderDatas[(material, geometry)] = []

        self.renderDatas[(material, geometry)].append((projection, view, model))

    def Render(self):
        for (material, geometry), array in self.renderDatas.items():
            if len(array) == 1:
                projection, view, model = array[0]
                geometry.Draw(material, projection, view, model)
            else:
                material.Use()
                models = []
                for projection, view, model in array:
                    models.append(model)
                    
                    # models.append(model[0, 0])
                    # models.append(model[0, 1])
                    # models.append(model[0, 2])
                    # models.append(model[0, 3])
                    # models.append(model[1, 0])
                    # models.append(model[1, 1])
                    # models.append(model[1, 2])
                    # models.append(model[1, 3])
                    # models.append(model[2, 0])
                    # models.append(model[2, 1])
                    # models.append(model[2, 2])
                    # models.append(model[2, 3])
                    # models.append(model[3, 0])
                    # models.append(model[3, 1])
                    # models.append(model[3, 2])
                    # models.append(model[3, 3])

                    # models.append(model[0, 0])
                    # models.append(model[1, 0])
                    # models.append(model[2, 0])
                    # models.append(model[3, 0])
                    # models.append(model[0, 1])
                    # models.append(model[1, 1])
                    # models.append(model[2, 1])
                    # models.append(model[3, 1])
                    # models.append(model[0, 2])
                    # models.append(model[1, 2])
                    # models.append(model[2, 2])
                    # models.append(model[3, 2])
                    # models.append(model[0, 3])
                    # models.append(model[1, 3])
                    # models.append(model[2, 3])
                    # models.append(model[3, 3])

                geometry.DrawInstanced(material, projection, view, models)

        self.renderDatas = {}