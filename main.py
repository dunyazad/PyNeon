from Neon.NGeometry import NGeometry
from Neon.NVertexArrayObject import NVertexArrayObject
from Neon.Neon import *

from TextureLoader import load_texture

cameraManipulator = None

# glfw callback functions
def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = glm.perspective(45, width / height, 0.1, 100)
    sceneLayer.GetCameraNode().SetProjectionMatrix(projection)
    glViewport(0, 0, width, height)

    # shader.UniformMatrix4fv("projection", glm.value_ptr(projection))

# stores which keys are pressed and handle key press in the main loop
keyArray = np.array([False] * 400, np.bool)

def window_keypress_callback(window, key, scanCode, action, mods):
    if key == glfw.KEY_UNKNOWN:
        return

    if action == glfw.PRESS:
        if key == glfw.KEY_ESCAPE:
            # respond escape here
            glfw.set_window_should_close(window, True)
        else:
            keyArray[key] = True
    elif action == glfw.RELEASE:
        keyArray[key] = False

def keyboard_respond_func():
    global keyArray
    global cameraManipulator

    keyPressed = np.where(keyArray == True)
    for key in keyPressed[0]:
        # if key in glfwKeyTranslator:
        # camera.respond_keypress(glfwKeyTranslator[key])
        cameraManipulator.OnKeyboardEvent(key)

cursorPos = None
def window_cursor_callback(window, xPos, yPos):
    global cursorPos
    global cameraManipulator
    xOffset = xPos - cursorPos[0]
    yOffset = yPos - cursorPos[1]
    # camera.respond_mouse_movement(xOffset, yOffset)
    cursorPos = (xPos, yPos)
    cameraManipulator.OnMousePositionEvent(xPos, yPos)

def window_scroll_callback(window, xOffset, yOffset):
    # camera.respond_scroll(yOffset)
    pass

def window_mouse_button_callback(window, button, action, mods):
    global cameraManipulator
    cameraManipulator.OnMouseButtonEvent(button, action, mods)

# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# set Anti Aliasing
# glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
# glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.SAMPLES, 8)

# creating the window
window = glfw.create_window(2560, 1440, "Neon window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

glfw.set_window_size_callback(window, window_resize)
glfw.make_context_current(window)
glfw.set_key_callback(window, window_keypress_callback)
glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)
glfw.set_cursor_pos_callback(window, window_cursor_callback)
glfw.set_mouse_button_callback(window, window_mouse_button_callback)
glfw.set_scroll_callback(window, window_scroll_callback)
cursorPos = glfw.get_cursor_pos(window)

# vsync off
# glfw.swap_interval(0)

renderer = NRenderer()

scene = NScene("Default")
sceneLayer = scene.CreateSceneLayer("Default")

cameraManipulator = NCameraManipulatorFPS(sceneLayer.GetCameraNode())
cameraManipulator.SetEyePosition(glm.vec3(0, 1, 0))
cameraManipulator.SetTargetPosition(glm.vec3(0, 1, -1))

sceneNodeCube1 = sceneLayer.CreateSceneNode("cube1")
sceneNodeCube2 = sceneLayer.CreateSceneNode("cube2")
sceneNodeCube3 = sceneLayer.CreateSceneNode("cube3")

geometryCube = NGeometry()
geometryCube.InitializeCube()

geometryPlane = NGeometry()
geometryPlane.InitializePlane()

defaultShader = NShader(open("shaders/default.vs"), open("shaders/default.fs"))

texture_cube1 = NTexture()
texture_cube1.LoadFromFile("textures/crate.jpg")
material_cube1 = NMaterial()
material_cube1.SetShader(defaultShader)
material_cube1.SetTexture(texture_cube1)
sceneNodeCube1.AddRenderData(material_cube1, geometryCube)
sceneNodeCube1.SetLocalTransform(glm.translate(glm.mat4(), glm.vec3(1, 0, 0)))

texture_cube2 = NTexture()
texture_cube2.LoadFromFile("textures/cat.png")
material_cube2 = NMaterial()
material_cube2.SetShader(defaultShader)
material_cube2.SetTexture(texture_cube2)
sceneNodeCube2.AddRenderData(material_cube2, geometryCube)
sceneNodeCube2.SetLocalTransform(glm.translate(glm.mat4(), glm.vec3(-1, 0, 0)))

texture_cube3 = NTexture()
texture_cube3.LoadFromFile("textures/smiley.png")
material_cube3 = NMaterial()
material_cube3.SetShader(defaultShader)
material_cube3.SetTexture(texture_cube3)
sceneNodeCube3.AddRenderData(material_cube3, geometryPlane)
sceneNodeCube3.SetLocalTransform(glm.translate(glm.mat4(), glm.vec3(0, 1, -3)))


cubeMaterial = NMaterial()
cubeShader = NShader(open("shaders/geometry_shader.vs"), open("shaders/geometry_shader.fs"), open("shaders/geometry_shader.gs"))
cubeMaterial.SetShader(cubeShader)
cubeTexture = NTexture()
cubeTexture.LoadFromFile("textures/paper.png")
cubeMaterial.SetTexture(cubeTexture)

shape = (1024,1024)
scale = 100
octaves = 6
persistence = 0.5
lacunarity = 2.0
seed = np.random.randint(0,100)
seed = 126

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=seed)

cubeGeometry = NGeometry()
cubeGeometry.SetDrawingMode(GL_POINTS)
rows = 1024
columns = 1024
layers = 1
for r in range(rows):
    for c in range(columns):
        for l in range(layers):
            nl = math.floor(world[r][c] * 50)
            cubeGeometry.AddVertex(glm.vec3(r, nl, c))
cubeGeometry.BuildRenderData()

for r in range(3):
    for c in range(3):
        for l in range(3):
            node = sceneLayer.CreateSceneNode("cubeNode" + str(r) + str(c) + str(l))
            node.AddRenderData(cubeMaterial, cubeGeometry)
            node.SetLocalTransform(glm.translate(glm.mat4(), glm.vec3(r * 1000, l * 1, c * 1000)))


# Instancing ==>>
# instancedCubeMaterial = NMaterial()

# instancedShader = NShader(open("shaders/instanced.vs"), open("shaders/instanced.fs"))
# instancedCubeMaterial.SetShader(instancedShader)

# crateTexture = NTexture()
# crateTexture.LoadFromFile("textures/crate.jpg")
# instancedCubeMaterial.SetTexture(crateTexture)

# for rr in range(2):
#     for cc in range(2):
#         for ll in range(2):
#             instancedCube = NGeometry()
#             instancedCube.InitializeCube(1)

#             instancedCubeSceneNodes = sceneLayer.CreateSceneNodeInstancing("instacing" + str(rr) + ", " + str(cc) + ", " + str(ll))
#             instancedCubeSceneNodes.AddRenderData(instancedCubeMaterial, instancedCube)

#             rows = 32
#             columns = 32
#             layers = 32
#             for r in range(rows):
#                 for c in range(columns):
#                     for l in range(layers):
#                         # cube = sceneLayer.CreateSceneNode("cube[" + str(r) + "," + str(c) + "]")
#                         # cube.AddRenderData(instancedCubeMaterial, instancedCube)
#                         # cube.SetLocalTransform(glm.translate(glm.mat4(), glm.vec3(c - columns * 0.5, -0.5, r - rows * 0.5)))
#                         instancedCubeSceneNodes.AddTransform(glm.translate(glm.mat4(1), glm.vec3(rr * 32, ll * 32, cc * 32)) * glm.translate(glm.mat4(), glm.vec3(c - columns * 0.5, l - layers * 0.5, r - rows * 0.5)))
# <<== Instancing

glClearColor(0, 0.1, 0.1, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

glEnable(GL_CULL_FACE)
glCullFace(GL_BACK)
# glFrontFace(GL_CCW)

now = time.time_ns()
lastTime = time.time_ns()
accTime = 0.0
frameCount = 0

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    # respond key press
    keyboard_respond_func()

    now = time.time_ns()
    timeDelta = now - lastTime
    lastTime = now
    accTime += timeDelta
    frameCount += 1
    if accTime >= 1000000000:
        print("frameCount : " + str(frameCount))
        accTime -= 1000000000
        frameCount = 0

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    rot_x = glm.rotate(glm.mat4(), 0.5 * glfw.get_time(), glm.vec3(1, 0, 0))
    rot_y = glm.rotate(glm.mat4(), 0.8 * glfw.get_time(), glm.vec3(0, 1, 0))

    rotation = rot_x * rot_y
    model = glm.translate(glm.mat4(), glm.vec3(1, 0, 0)) * rotation

    sceneNodeCube1.SetLocalTransform(model)

    model = glm.rotate(glm.translate(glm.mat4(), glm.vec3(-1, 0, 0)), 0.5 * glfw.get_time(), glm.vec3(1, 0, 0))
    sceneNodeCube2.SetLocalTransform(model)

    model = glm.rotate(glm.translate(glm.mat4(), glm.vec3(0, 1, -3)), 0.8 * glfw.get_time(), glm.vec3(0, 1, 0))
    sceneNodeCube3.SetLocalTransform(model)

    scene.Update(timeDelta)
    scene.Render(renderer)

    renderer.Render()

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()
