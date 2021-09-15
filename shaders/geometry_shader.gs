#version 330 core
#extension GL_ARB_geometry_shader4 : enable
layout (points) in;
layout (triangle_strip, max_vertices = 24) out;

uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;

out vec2 TexCoords;

void GenerateVertex(in vec4 offset, in vec2 uv);

void main() {
    GenerateVertex(vec4(-0.5, -0.5, 0.5, 0.0), vec2(0.0, 0.0));
    GenerateVertex(vec4( 0.5, -0.5, 0.5, 0.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(-0.5,  0.5, 0.5, 0.0), vec2(0.0, 1.0));
    GenerateVertex(vec4( 0.5,  0.5, 0.5, 0.0), vec2(1.0, 1.0));
    EndPrimitive();

    GenerateVertex(vec4(-0.5, -0.5, -0.5, 0.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(-0.5,  0.5, -0.5, 0.0), vec2(1.0, 1.0));
    GenerateVertex(vec4( 0.5, -0.5, -0.5, 0.0), vec2(0.0, 0.0));
    GenerateVertex(vec4( 0.5,  0.5, -0.5, 0.0), vec2(0.0, 1.0));
    EndPrimitive();

    GenerateVertex(vec4(0.5, -0.5, -0.5, 0.0), vec2(0.0, 0.0));
    GenerateVertex(vec4(0.5,  0.5, -0.5, 0.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(0.5, -0.5,  0.5, 0.0), vec2(0.0, 1.0));
    GenerateVertex(vec4(0.5,  0.5,  0.5, 0.0), vec2(1.0, 1.0));
    EndPrimitive();

    GenerateVertex(vec4(-0.5, -0.5, -0.5, 0.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(-0.5, -0.5,  0.5, 0.0), vec2(1.0, 1.0));
    GenerateVertex(vec4(-0.5,  0.5, -0.5, 0.0), vec2(0.0, 0.0));
    GenerateVertex(vec4(-0.5,  0.5,  0.5, 0.0), vec2(0.0, 1.0));
    EndPrimitive();

    GenerateVertex(vec4(-0.5, -0.5, -0.5, 0.0), vec2(0.0, 0.0));
    GenerateVertex(vec4( 0.5, -0.5, -0.5, 0.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(-0.5, -0.5,  0.5, 0.0), vec2(0.0, 1.0));
    GenerateVertex(vec4( 0.5, -0.5,  0.5, 0.0), vec2(1.0, 1.0));
    EndPrimitive();

    GenerateVertex(vec4(-0.5, 0.5, -0.5, 0.0), vec2(1.0, 0.0));
    GenerateVertex(vec4(-0.5, 0.5,  0.5, 0.0), vec2(1.0, 1.0));
    GenerateVertex(vec4( 0.5, 0.5, -0.5, 0.0), vec2(0.0, 0.0));
    GenerateVertex(vec4( 0.5, 0.5,  0.5, 0.0), vec2(0.0, 1.0));
    EndPrimitive();
}

void GenerateVertex(in vec4 offset, in vec2 uv) {
    vec4 vertexPos = offset + gl_in[0].gl_Position;
    gl_Position = projection * view * model * vertexPos;
    TexCoords = uv;
    EmitVertex();
}
