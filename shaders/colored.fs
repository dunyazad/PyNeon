# version 330
in vec2 v_uv;
in vec4 v_color;
out vec4 out_color;
uniform sampler2D s_texture;
void main()
{
    out_color = v_color;
}
