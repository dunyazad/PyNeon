from .NCommon import *

from .NShader import *
from .NTexture import *

class NMaterial():
    def __init__(self) -> None:
        self.shader = None
        self.texture = None

    def SetShader(self, shader):
        self.shader = shader

    def SetTexture(self, texture):
        self.texture = texture

    def Use(self):
        if self.shader is not None:
            self.shader.Use()

        if self.texture is not None:
            self.texture.Bind()