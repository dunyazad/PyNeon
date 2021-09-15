# version 330
in vec2 TexCoords;
out vec4 out_color;
uniform sampler2D s_texture;
void main()
{
    out_color = texture(s_texture, TexCoords);
    // out_color = vec4(1, 1, 1, 1);
    // out_color = Color;
}
