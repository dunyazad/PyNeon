from Neon.NGeometry import NGeometry
from Neon.NVertexArrayObject import NVertexArrayObject
from Neon.Neon import *

from TextureLoader import load_texture

shader = None

vertex_src = """
# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;
out vec3 v_color;
out vec2 v_texture;
void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

fragment_src = """
# version 330
in vec2 v_texture;
out vec4 out_color;
uniform sampler2D s_texture;
void main()
{
    out_color = texture(s_texture, v_texture);
}
"""


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

geometry.vertices = [-0.5, -0.5,  0.5, 0.0, 0.0,
             0.5, -0.5,  0.5, 1.0, 0.0,
             0.5,  0.5,  0.5, 1.0, 1.0,
            -0.5,  0.5,  0.5, 0.0, 1.0,

            -0.5, -0.5, -0.5, 0.0, 0.0,
             0.5, -0.5, -0.5, 1.0, 0.0,
             0.5,  0.5, -0.5, 1.0, 1.0,
            -0.5,  0.5, -0.5, 0.0, 1.0,

             0.5, -0.5, -0.5, 0.0, 0.0,
             0.5,  0.5, -0.5, 1.0, 0.0,
             0.5,  0.5,  0.5, 1.0, 1.0,
             0.5, -0.5,  0.5, 0.0, 1.0,

            -0.5,  0.5, -0.5, 0.0, 0.0,
            -0.5, -0.5, -0.5, 1.0, 0.0,
            -0.5, -0.5,  0.5, 1.0, 1.0,
            -0.5,  0.5,  0.5, 0.0, 1.0,

            -0.5, -0.5, -0.5, 0.0, 0.0,
             0.5, -0.5, -0.5, 1.0, 0.0,
             0.5, -0.5,  0.5, 1.0, 1.0,
            -0.5, -0.5,  0.5, 0.0, 1.0,

             0.5, 0.5, -0.5, 0.0, 0.0,
            -0.5, 0.5, -0.5, 1.0, 0.0,
            -0.5, 0.5,  0.5, 1.0, 1.0,
             0.5, 0.5,  0.5, 0.0, 1.0]

geometry.indices = [ 0,  1,  2,  2,  3,  0,
            4,  5,  6,  6,  7,  4,
            8,  9, 10, 10, 11,  8,
           12, 13, 14, 14, 15, 12,
           16, 17, 18, 18, 19, 16,
           20, 21, 22, 22, 23, 20]

vertices = np.array(geometry.vertices, dtype=np.float32)
indices = np.array(geometry.indices, dtype=np.uint32)

shader = NShader(vertex_src, fragment_src)

VAO = NVertexArrayObject()
VAO.Bind()

VBO = NVertexBufferObject()
VBO.Bind()
VBO.BufferData(vertices.nbytes, vertices)

EBO = NElementBufferObject()
EBO.Bind()
EBO.BufferData(indices.nbytes, indices)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, vertices.itemsize * 5, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, vertices.itemsize * 5, ctypes.c_void_p(12))

textures = [NTexture(), NTexture(), NTexture()]

cube1_texture = NTexture()
cube1_texture.LoadFromFile("textures/crate.jpg")

cube2_texture = NTexture()
cube2_texture.LoadFromFile("textures/cat.png")

cube3_texture = NTexture()
cube3_texture.LoadFromFile("textures/smiley.png")

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

    cube1_texture.Bind()
    shader.UniformMatrix4fv("model", glm.value_ptr(model))
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    # model = pyrr.matrix44.multiply(rot_x, cube2)
    model = glm.rotate(cube2, 0.5 * glfw.get_time(), glm.vec3(1, 0, 0))

    cube2_texture.Bind()
    shader.UniformMatrix4fv("model", glm.value_ptr(model))
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    # model = pyrr.matrix44.multiply(rot_y, cube3)
    model = glm.rotate(cube3, 0.8 * glfw.get_time(), glm.vec3(0, 1, 0))

    cube3_texture.Bind()
    shader.UniformMatrix4fv("model", glm.value_ptr(model))
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

    shader.Unuse()

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()
