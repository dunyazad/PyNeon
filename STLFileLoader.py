import glm

class STLFileLoader:
    def __init__(self):
        pass

    def Load(self, fileName):
        isASCII = self.CheckIsBinary(fileName)
        if isASCII:
            return self.LoadASCII(fileName)

    def CheckIsBinary(self, fileName):
        f = open(fileName)

        line = f.readline()
        f.close()

        words = line.split()
        if words[0] == "solid":
            return True
        else:
            return False
    
    def LoadASCII(self, fileName):
        f = open(fileName)
        line = f.readline()

        normals = []
        vertices = []
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
                vertices.append(glm.vec3(float(words[1]), float(words[2]), float(words[3])))
                normals.append(normal)
        f.close()

        return vertices, normals, indices