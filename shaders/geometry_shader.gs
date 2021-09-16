#version 330 core
#extension GL_ARB_geometry_shader4 : enable
layout (points) in;
// layout (invocations = num_instances) in;
layout (triangle_strip, max_vertices = 24) out;

uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;

out vec3 FragPos;
out vec2 TexCoords;
out vec3 Normal;

void GenerateVertex(in vec4 offset, in vec3 normal, in vec2 uv) {
    vec4 vertexPos = offset + gl_in[0].gl_Position;
    gl_Position = projection * view * model * vertexPos;
    FragPos = vec3(view * model * vertexPos);
    TexCoords = uv;
    Normal = vec3(view * model * vec4(normal, 0.0));
    EmitVertex();
}

void main() {
    GenerateVertex(vec4(-0.5, -0.5, 0.5, 0.0), vec3(0.0, 0.0, 1.0), vec2(0.0, 0.0));
    GenerateVertex(vec4( 0.5, -0.5, 0.5, 0.0), vec3(0.0, 0.0, 1.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(-0.5,  0.5, 0.5, 0.0), vec3(0.0, 0.0, 1.0), vec2(0.0, 1.0));
    GenerateVertex(vec4( 0.5,  0.5, 0.5, 0.0), vec3(0.0, 0.0, 1.0), vec2(1.0, 1.0));
    EndPrimitive();

    GenerateVertex(vec4(-0.5, -0.5, -0.5, 0.0), vec3(0.0, 0.0, -1.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(-0.5,  0.5, -0.5, 0.0), vec3(0.0, 0.0, -1.0), vec2(1.0, 1.0));
    GenerateVertex(vec4( 0.5, -0.5, -0.5, 0.0), vec3(0.0, 0.0, -1.0), vec2(0.0, 0.0));
    GenerateVertex(vec4( 0.5,  0.5, -0.5, 0.0), vec3(0.0, 0.0, -1.0), vec2(0.0, 1.0));
    EndPrimitive();

    GenerateVertex(vec4(0.5, -0.5, -0.5, 0.0), vec3(1.0, 0.0, 0.0), vec2(0.0, 0.0));
    GenerateVertex(vec4(0.5,  0.5, -0.5, 0.0), vec3(1.0, 0.0, 0.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(0.5, -0.5,  0.5, 0.0), vec3(1.0, 0.0, 0.0), vec2(0.0, 1.0));
    GenerateVertex(vec4(0.5,  0.5,  0.5, 0.0), vec3(1.0, 0.0, 0.0), vec2(1.0, 1.0));
    EndPrimitive();

    GenerateVertex(vec4(-0.5, -0.5, -0.5, 0.0), vec3(-1.0, 0.0, 0.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(-0.5, -0.5,  0.5, 0.0), vec3(-1.0, 0.0, 0.0), vec2(1.0, 1.0));
    GenerateVertex(vec4(-0.5,  0.5, -0.5, 0.0), vec3(-1.0, 0.0, 0.0), vec2(0.0, 0.0));
    GenerateVertex(vec4(-0.5,  0.5,  0.5, 0.0), vec3(-1.0, 0.0, 0.0), vec2(0.0, 1.0));
    EndPrimitive();

    GenerateVertex(vec4(-0.5, -0.5, -0.5, 0.0), vec3(0.0, -1.0, 0.0), vec2(0.0, 0.0));
    GenerateVertex(vec4( 0.5, -0.5, -0.5, 0.0), vec3(0.0, -1.0, 0.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(-0.5, -0.5,  0.5, 0.0), vec3(0.0, -1.0, 0.0), vec2(0.0, 1.0));
    GenerateVertex(vec4( 0.5, -0.5,  0.5, 0.0), vec3(0.0, -1.0, 0.0), vec2(1.0, 1.0));
    EndPrimitive();

    GenerateVertex(vec4(-0.5, 0.5, -0.5, 0.0), vec3(0.0, 1.0, 0.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(-0.5, 0.5,  0.5, 0.0), vec3(0.0, 1.0, 0.0), vec2(1.0, 1.0));
    GenerateVertex(vec4( 0.5, 0.5, -0.5, 0.0), vec3(0.0, 1.0, 0.0), vec2(0.0, 0.0));
    GenerateVertex(vec4( 0.5, 0.5,  0.5, 0.0), vec3(0.0, 1.0, 0.0), vec2(0.0, 1.0));
    EndPrimitive();
}

