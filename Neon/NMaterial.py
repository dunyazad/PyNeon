from .NCommon import *

from .NShader import *
from .NTexture import *

class NMaterial():
    def __init__(self) -> None:
        self.shader = None
        self.texture = None

    def GetShader(self):
        return self.shader

    def SetShader(self, shader):
        self.shader = shader

    def SetTexture(self, texture):
        self.texture = texture

    def Use(self):
        if self.shader is not None:
            self.shader.Use()

        if self.texture is not None:
            self.texture.Bind()
    
    def Unuse(self):
        if self.shader is not None:
            self.shader.Unuse()

        if self.texture is not None:
            self.texture.Unbind()