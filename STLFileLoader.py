import glm

class STLFileLoader:
    def __init__(self):
        pass

    def Load(self, fileName, transform = glm.mat4(), color = glm.vec4(1.0, 1.0, 1.0, 1.0)):
        isASCII = self.CheckIsBinary(fileName)
        if isASCII:
            return self.LoadASCII(fileName, transform, color)

    def CheckIsBinary(self, fileName):
        f = open(fileName)

        line = f.readline()
        f.close()

        words = line.split()
        if words[0] == "solid":
            return True
        else:
            return False
    
    def LoadASCII(self, fileName, transform, color):
        f = open(fileName)
        line = f.readline()

        normals = []
        vertices = []
        colors = []
        indices = []

        normal = None

        while True:
            line = f.readline()
            if not line: 
                break
            
            words = line.split()
            if "facet" == words[0]:
                normal = glm.vec3(float(words[2]), float(words[3]), float(words[4]))
            elif "vertex" == words[0]:
                indices.append(len(vertices))
                vertices.append(glm.vec3(transform * glm.vec4(float(words[1]), float(words[2]), float(words[3]), 1.0)))
                normals.append(normal)
                colors.append(color)
        f.close()

        return vertices, normals, colors, indices