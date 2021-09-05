from .NCommon import *

class NVertexArrayObject():
    def __init__(self) -> None:
        self.arrayObject = glGenVertexArrays(1)

    def Bind(self):
        glBindVertexArray(self.arrayObject)

    def Unbind(self):
        glBindVertexArray(0)
