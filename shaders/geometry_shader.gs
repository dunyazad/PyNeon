#version 330 core
layout (points) in;
layout (triangle_strip, max_vertices = 36) out;

uniform mat4 vp;

out vec2 TexCoords;
out vec4 Color;

void main() {
    gl_Position = vec4(0, 0, 0, 0);
    Color = gl_in[0].gl_Position;
    EmitVertex();

    gl_Position = vec4(0, 1, 0, 0);
    //Color = gl_in[0].gl_Position + vp * vec4(0, 1, 0, 1);
    Color = vec4(0, 1, 0, 1);
    EmitVertex();

    gl_Position = vec4(1, 0, 0, 0);
    // Color = gl_in[0].gl_Position + vp * vec4(1, 0, 0, 1);
    Color = vec4(1, 0, 0, 1);
    EmitVertex();

    EndPrimitive();
}
