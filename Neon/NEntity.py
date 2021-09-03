from .NCommon import *

class NEntity:
    def __init__(self):
        self.rotation = glm.quat()
        self.translation = glm.vec3()