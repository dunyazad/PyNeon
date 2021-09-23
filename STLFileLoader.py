import glm

class STLFileLoader:
    def __init__(self):
        pass

    def Load(self, fileName, scale = glm.vec3(1.0, 1.0, 1.0), color = glm.vec4(1.0, 1.0, 1.0, 1.0)):
        isASCII = self.CheckIsBinary(fileName)
        if isASCII:
            return self.LoadASCII(fileName, scale, color)

    def CheckIsBinary(self, fileName):
        f = open(fileName)

        line = f.readline()
        f.close()

        words = line.split()
        if words[0] == "solid":
            return True
        else:
            return False
    
    def LoadASCII(self, fileName, scale, color):
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
                vertices.append(glm.vec3(float(words[1]) * scale.x, float(words[2]) * scale.y, float(words[3]) * scale.z))
                normals.append(normal)
                colors.append(color)
        f.close()

        return vertices, normals, colors, indices