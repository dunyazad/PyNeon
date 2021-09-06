from Neon.NGeometry import NGeometry
from Neon.NVertexArrayObject import NVertexArrayObject
from Neon.Neon import *

from TextureLoader import load_texture

# glfw callback functions
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = glm.perspective(45, width / height, 0.1, 100)
    # shader.UniformMatrix4fv("projection", glm.value_ptr(projection))

# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# creating the window
window = glfw.create_window(1280, 720, "Neon window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

# set the callback function for window resize
glfw.set_window_size_callback(window, window_resize)

# make the context current
glfw.make_context_current(window)

scene = NScene("Default")
sceneLayer = scene.CreateSceneLayer("Default")
sceneNodeCube1 = sceneLayer.CreateSceneNode("cube1")
sceneNodeCube2 = sceneLayer.CreateSceneNode("cube2")
sceneNodeCube3 = sceneLayer.CreateSceneNode("cube3")

geometry = NGeometry()
geometry.InitializeCube()
geometry.BuildRenderData()

vertex_src = open("shaders/default.vs")
fragment_src = open("shaders/default.fs")
shader = NShader(vertex_src, fragment_src)

texture_cube1 = NTexture()
texture_cube1.LoadFromFile("textures/crate.jpg")
material_cube1 = NMaterial()
material_cube1.SetShader(shader)
material_cube1.SetTexture(texture_cube1)
sceneNodeCube1.AddRenderData(material_cube1, geometry)
sceneNodeCube1.SetLocalTransform(glm.translate(glm.mat4(), glm.vec3(1, 0, 0)))

texture_cube2 = NTexture()
texture_cube2.LoadFromFile("textures/cat.png")
material_cube2 = NMaterial()
material_cube2.SetShader(shader)
material_cube2.SetTexture(texture_cube2)
sceneNodeCube2.AddRenderData(material_cube2, geometry)
sceneNodeCube2.SetLocalTransform(glm.translate(glm.mat4(), glm.vec3(-1, 0, 0)))

texture_cube3 = NTexture()
texture_cube3.LoadFromFile("textures/smiley.png")
material_cube3 = NMaterial()
material_cube3.SetShader(shader)
material_cube3.SetTexture(texture_cube3)
sceneNodeCube3.AddRenderData(material_cube3, geometry)
sceneNodeCube3.SetLocalTransform(glm.translate(glm.mat4(), glm.vec3(0, 1, -3)))

glClearColor(0, 0.1, 0.1, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    scene.Update(0)
    scene.Render()

    rot_x = glm.rotate(glm.mat4(), 0.5 * glfw.get_time(), glm.vec3(1, 0, 0))
    rot_y = glm.rotate(glm.mat4(), 0.8 * glfw.get_time(), glm.vec3(0, 1, 0))

    rotation = rot_x * rot_y
    model = glm.translate(glm.mat4(), glm.vec3(1, 0, 0)) * rotation

    sceneNodeCube1.SetLocalTransform(model)

    model = glm.rotate(glm.translate(glm.mat4(), glm.vec3(-1, 0, 0)), 0.5 * glfw.get_time(), glm.vec3(1, 0, 0))
    sceneNodeCube2.SetLocalTransform(model)

    model = glm.rotate(glm.translate(glm.mat4(), glm.vec3(0, 1, -3)), 0.8 * glfw.get_time(), glm.vec3(0, 1, 0))
    sceneNodeCube3.SetLocalTransform(model)

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()
