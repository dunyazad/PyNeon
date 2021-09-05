from .NCommon import *

class NShader():
    def __init__(self, vertexShaderCode, fragmentShaderCode) -> None:
        vs = compileShader(vertexShaderCode, GL_VERTEX_SHADER)
        fs = compileShader(fragmentShaderCode, GL_FRAGMENT_SHADER)
        self.shaderObject = compileProgram(vs, fs)
        self.uniforms = {}
    
    def GetShaderObject(self):
        return self.shaderObject

    def Use(self):
        glUseProgram(self.shaderObject)

    def Unuse(self):
        glUseProgram(0)

    def GetUniformLocation(self, uniformName):
        if uniformName not in self.uniforms:
            self.uniforms[uniformName] = glGetUniformLocation(self.shaderObject, uniformName)

        return self.uniforms[uniformName]

    def UniformMatrix4fv(self, uniformName, m):
        location = self.GetUniformLocation(uniformName)
        glUniformMatrix4fv(location, 1, False, m)
