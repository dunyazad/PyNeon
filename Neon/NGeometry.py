from .NCommon import *
from .NVertexArrayObject import *
from .NVertexBufferObject import *
from .NElementBufferObject import *

class NGeometry():
    def __init__(self) -> None:
        self.vertices = []
        self.normals = []
        self.uvs = []
        self.colors = []
        self.indices = []

        self.vertexArrayObject = None
        self.vertexBuffer = None
        self.normalBuffer = None
        self.uvBuffer = None
        self.colorBuffer = None
        self.indexBuffer = None

    def SetVertices(self, vertices):
        self.vertices = vertices

    def SetNormals(self, normals):
        self.normals = normals

    def SetUVs(self, uvs):
        self.uvs = uvs

    def SetColors(self, colors):
        self.colors = colors

    def SetIndices(self, indices):
        self.indices = indices

    def BuildRenderData(self):
        vertices = np.array(self.vertices, dtype=np.float32)
        normals = np.array(self.normals, dtype=np.float32)
        uvs = np.array(self.uvs, dtype=np.float32)
        colors = np.array(self.colors, dtype=np.float32)
        indices = np.array(self.indices, dtype=np.uint32)

        self.vertexArrayObject = NVertexArrayObject()
        self.vertexArrayObject.Bind()

        self.vertexBuffer = NVertexBufferObject()
        self.vertexBuffer.Bind()
        self.vertexBuffer.BufferData(vertices.nbytes, vertices)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        self.normalBuffer = NVertexBufferObject()
        self.normalBuffer.Bind()
        self.normalBuffer.BufferData(normals.nbytes, normals)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        self.uvBuffer = NVertexBufferObject()
        self.uvBuffer.Bind()
        self.uvBuffer.BufferData(uvs.nbytes, uvs)
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        self.colorBuffer = NVertexBufferObject()
        self.colorBuffer.Bind()
        self.colorBuffer.BufferData(colors.nbytes, colors)
        glEnableVertexAttribArray(3)
        glVertexAttribPointer(3, 4, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        self.indexBuffer = NElementBufferObject()
        self.indexBuffer.Bind()
        self.indexBuffer.BufferData(indices.nbytes, indices)

    def Draw(self, material, projection, view, model):
        self.vertexArrayObject.Bind()

        # self.vertexBuffer.Bind()
        # glEnableVertexAttribArray(0)
        # glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        # self.normalBuffer.Bind()
        # glEnableVertexAttribArray(1)
        # glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        # self.uvBuffer.Bind()
        # glEnableVertexAttribArray(2)
        # glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        # self.colorBuffer.Bind()
        # glEnableVertexAttribArray(3)
        # glVertexAttribPointer(3, 4, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

        # self.indexBuffer.Bind()

        material.Use()
        material.GetShader().UniformMatrix4fv("projection", glm.value_ptr(projection))
        material.GetShader().UniformMatrix4fv("view", glm.value_ptr(view))
        material.GetShader().UniformMatrix4fv("model", glm.value_ptr(model))
        glDrawElements(GL_TRIANGLES, len(self.indices), GL_UNSIGNED_INT, None)
        material.Unuse()

        # self.vertexBuffer.Unbind()
        # self.normalBuffer.Unbind()
        # self.uvBuffer.Unbind()
        # self.colorBuffer.Unbind()
        # self.indexBuffer.Unbind()
        
        self.vertexArrayObject.Unbind()

    def InitializeCube(self):
        self.vertices = [
            -0.5, -0.5,  0.5,
             0.5, -0.5,  0.5,
             0.5,  0.5,  0.5,
            -0.5,  0.5,  0.5,

            -0.5, -0.5, -0.5,
             0.5, -0.5, -0.5,
             0.5,  0.5, -0.5,
            -0.5,  0.5, -0.5,

             0.5, -0.5, -0.5,
             0.5,  0.5, -0.5,
             0.5,  0.5,  0.5,
             0.5, -0.5,  0.5,

            -0.5,  0.5, -0.5,
            -0.5, -0.5, -0.5,
            -0.5, -0.5,  0.5,
            -0.5,  0.5,  0.5,

            -0.5, -0.5, -0.5,
             0.5, -0.5, -0.5,
             0.5, -0.5,  0.5,
            -0.5, -0.5,  0.5,

             0.5,  0.5, -0.5,
            -0.5,  0.5, -0.5,
            -0.5,  0.5,  0.5,
             0.5,  0.5,  0.5]

        self.normals = [
            0.0, 0.0, 1.0,
            0.0, 0.0, 1.0,
            0.0, 0.0, 1.0,
            0.0, 0.0, 1.0,

            0.0, 0.0, -1.0,
            0.0, 0.0, -1.0,
            0.0, 0.0, -1.0,
            0.0, 0.0, -1.0,

            1.0, 0.0, 0.0,
            1.0, 0.0, 0.0,
            1.0, 0.0, 0.0,
            1.0, 0.0, 0.0,

            -1.0, 0.0, 0.0,
            -1.0, 0.0, 0.0,
            -1.0, 0.0, 0.0,
            -1.0, 0.0, 0.0,

            0.0, -1.0, 0.0,
            0.0, -1.0, 0.0,
            0.0, -1.0, 0.0,
            0.0, -1.0, 0.0,

            0.0, 1.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 1.0, 0.0,
            0.0, 1.0, 0.0]

        self.uvs = [
            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,

            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,

            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,

            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,

            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0,

            0.0, 0.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 1.0]

        self.colors = [
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,

            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,

            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,

            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0]

        self.indices = [
            0,  1,  2,  2,  3,  0,
            4,  5,  6,  6,  7,  4,
            8,  9, 10, 10, 11,  8,
            12, 13, 14, 14, 15, 12,
            16, 17, 18, 18, 19, 16,
            20, 21, 22, 22, 23, 20]
