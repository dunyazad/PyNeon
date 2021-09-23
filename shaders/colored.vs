# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec3 a_normal;
layout(location = 2) in vec2 a_uv;
layout(location = 4) in vec4 a_color;

uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;
uniform vec3 viewPos;
uniform vec3 lightPos;
out vec4 v_color;
out vec2 v_uv;

void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_uv = a_uv;
    v_color = a_color;
}
