# version 330
in vec3 FragPos;
in vec2 TexCoords;
in vec3 Normal;

out vec4 out_color;
uniform sampler2D s_texture;
uniform vec3 lightPos; 
uniform vec3 viewPos;
void main()
{
    // out_color = texture(s_texture, TexCoords);

    // out_color = vec4(1, 1, 1, 1);
    // out_color = Color;

    vec3 lightColor = vec3(1.0, 1.0, 1.0);

    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;
  	
    // diffuse 
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;
    
    // specular
    float specularStrength = 0.0125;
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);  
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
    vec3 specular = specularStrength * lightColor;
        
    vec3 result = (ambient + diffuse + specular);
    out_color = texture(s_texture, TexCoords) * vec4(result, 1.0);
}
