from .NCommon import *

class NShader():
    def __init__(self, vertexShaderCode, fragmentShaderCode, geometryShaderCode = None) -> None:
        vs = compileShader(vertexShaderCode, GL_VERTEX_SHADER)
        fs = compileShader(fragmentShaderCode, GL_FRAGMENT_SHADER)
        if geometryShaderCode is not None:
            gs = compileShader(geometryShaderCode, GL_GEOMETRY_SHADER)
            self.shaderObject = compileProgram(vs, fs, gs)
        else:
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

    def Uniform3f(self, uniformName, v):
        location = self.GetUniformLocation(uniformName)
        if location != -1:
            glUniform3f(location, v.x, v.y, v.z)

    def UniformMatrix4fv(self, uniformName, m):
        location = self.GetUniformLocation(uniformName)
        if location != -1:
            glUniformMatrix4fv(location, 1, False, m)
