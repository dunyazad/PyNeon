from .NCommon import *

class NVertexBufferObject():
    def __init__(self) -> None:
        self.bufferObject = glGenBuffers(1)

    def Bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferObject)

    def Unbind(self):
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def BufferData(self, dataSize, data):
        glBufferData(GL_ARRAY_BUFFER, dataSize, data, GL_STATIC_DRAW)
