from .NCommon import *

class NTexture():
    def __init__(self) -> None:
        self.textureObject = glGenTextures(1)

    # for use with GLFW
    def LoadFromFile(self, path):
        glBindTexture(GL_TEXTURE_2D, self.textureObject)
        # Set the texture wrapping parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        # Set texture filtering parameters
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        # load image
        image = Image.open(path)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    def Bind(self):
        glBindTexture(GL_TEXTURE_2D, self.textureObject)

    def Unbind(self):
        glBindTexture(GL_TEXTURE_2D, 0)