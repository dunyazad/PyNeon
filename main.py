from Neon.NGeometry import NGeometry
from Neon.NVertexArrayObject import NVertexArrayObject
from Neon.Neon import *

from TextureLoader import load_texture

shader = None

# glfw callback functions
def window_resize(window, width, height):
    global shader

    glViewport(0, 0, width, height)
    # projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
    projection = glm.perspective(45, width / height, 0.1, 100)
    # glUniformMatrix4fv(proj_loc, 1, GL_FALSE, glm.value_ptr(projection))
    shader.UniformMatrix4fv("projection", glm.value_ptr(projection))

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

geometry = NGeometry()
geometry.InitializeCube()

vertices = np.array(geometry.vertices, dtype=np.float32)
uvs = np.array(geometry.uvs, dtype=np.float32)
indices = np.array(geometry.indices, dtype=np.uint32)

VAO = NVertexArrayObject()
VAO.Bind()

VBO = NVertexBufferObject()
VBO.Bind()
VBO.BufferData(vertices.nbytes, vertices)
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

UVBO = NVertexBufferObject()
UVBO.Bind()
UVBO.BufferData(uvs.nbytes, uvs)
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))

EBO = NElementBufferObject()
EBO.Bind()
EBO.BufferData(indices.nbytes, indices)

vertex_src = open("shaders/default.vs")
fragment_src = open("shaders/default.fs")
shader = NShader(vertex_src, fragment_src)

texture_cube1 = NTexture()
texture_cube1.LoadFromFile("textures/crate.jpg")
material_cube1 = NMaterial()
material_cube1.SetShader(shader)
material_cube1.SetTexture(texture_cube1)

texture_cube2 = NTexture()
texture_cube2.LoadFromFile("textures/cat.png")
material_cube2 = NMaterial()
material_cube2.SetShader(shader)
material_cube2.SetTexture(texture_cube2)

texture_cube3 = NTexture()
texture_cube3.LoadFromFile("textures/smiley.png")
material_cube3 = NMaterial()
material_cube3.SetShader(shader)
material_cube3.SetTexture(texture_cube3)

glClearColor(0, 0.1, 0.1, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

# projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280/720, 0.1, 100)
projection = glm.perspective(glm.radians(45), 1280/720, 0.1, 100)
# cube1 = pyrr.matrix44.create_from_translation(pyrr.Vector3([1, 0, 0]))
cube1 = glm.translate(glm.mat4(), glm.vec3(1, 0, 0))
# cube2 = pyrr.matrix44.create_from_translation(pyrr.Vector3([-1, 0, 0]))
cube2 = glm.translate(glm.mat4(), glm.vec3(-1, 0, 0))
# cube3 = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 1, -3]))
cube3 = glm.translate(glm.mat4(), glm.vec3(0, 1, -3))

# eye, target, up
# view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 3]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))
view = glm.lookAt(glm.vec3(0, 0, 3), glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))

model = glm.mat4()

shader.Use()

shader.UniformMatrix4fv("projection", glm.value_ptr(projection))
shader.UniformMatrix4fv("view", glm.value_ptr(view))
shader.UniformMatrix4fv("model", glm.value_ptr(model))

shader.Unuse()

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    shader.Use()

    # rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time())
    rot_x = glm.rotate(glm.mat4(), 0.5 * glfw.get_time(), glm.vec3(1, 0, 0))
    # rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())
    rot_y = glm.rotate(glm.mat4(), 0.8 * glfw.get_time(), glm.vec3(0, 1, 0))

    # rotation = pyrr.matrix44.multiply(rot_x, rot_y)
    rotation = rot_x * rot_y
    # model = pyrr.matrix44.multiply(rotation, cube1)
    model = glm.translate(glm.mat4(), glm.vec3(1, 0, 0)) * rotation

    material_cube1.Use()
    shader.UniformMatrix4fv("model", glm.value_ptr(model))
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    # model = pyrr.matrix44.multiply(rot_x, cube2)
    model = glm.rotate(cube2, 0.5 * glfw.get_time(), glm.vec3(1, 0, 0))

    material_cube2.Use()
    shader.UniformMatrix4fv("model", glm.value_ptr(model))
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    # model = pyrr.matrix44.multiply(rot_y, cube3)
    model = glm.rotate(cube3, 0.8 * glfw.get_time(), glm.vec3(0, 1, 0))

    material_cube3.Use()
    shader.UniformMatrix4fv("model", glm.value_ptr(model))
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    shader.Unuse()

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()
