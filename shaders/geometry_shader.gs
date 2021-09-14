#version 330 core
#extension GL_ARB_geometry_shader4 : enable
layout (points) in;
layout (triangle_strip, max_vertices = 4) out;

uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;

// out vec2 TexCoords;
out vec4 Color;

void main() {
    {
    vec4 offset = vec4(-0.5, -0.5, 0.0, 0.0);
    vec4 vertexPos = offset + gl_in[0].gl_Position;
    gl_Position = projection * view * vertexPos;
    // gl_Position = vertexPos;
    Color = vec4(1, 0, 0, 1);
    EmitVertex();
    }

    {
    vec4 offset = vec4(-0.5, 0.5, 0.0, 0.0);
    vec4 vertexPos = offset + gl_in[0].gl_Position;
    gl_Position = projection * view * vertexPos;
    // gl_Position = vertexPos;
    Color = vec4(1, 0, 0, 1);
    EmitVertex();
    }

    {
    vec4 offset = vec4(0.5, -0.5, 0.0, 0.0);
    vec4 vertexPos = offset + gl_in[0].gl_Position;
    gl_Position = projection * view * vertexPos;
    // gl_Position = vertexPos;
    Color = vec4(1, 0, 0, 1);
    EmitVertex();
    }

    {
    vec4 offset = vec4(0.5, 0.5, 0.0, 0.0);
    vec4 vertexPos = offset + gl_in[0].gl_Position;
    gl_Position = projection * view * vertexPos;
    // gl_Position = vertexPos;
    Color = vec4(1, 0, 0, 1);
    EmitVertex();
    }

    EndPrimitive();
}
