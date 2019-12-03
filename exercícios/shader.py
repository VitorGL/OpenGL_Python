from OpenGL.GL import *
from OpenGL.GL import shaders as sh
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import ctypes

# Shader object
shader = None
vertexbuffer = None
shaderProgram = None


def main():

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow("Basic Shader Example")
    init()
    glutIdleFunc(idle)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)

    print("Pressione ESC para fechar.")
    print(glGetString(GL_VERSION))
    glutMainLoop()


def cria_shader(fonte_vertice, fonte_fragment):
    v = sh.compileShader(fonte_vertice, GL_VERTEX_SHADER)
    f = sh.compileShader(fonte_fragment, GL_FRAGMENT_SHADER)
    shader = sh.compileProgram(v, f)

    return shader


def getUniLoc(program, name):

    loc = glGetUniformLocation(program, name)
    if loc == -1:
        print("No such uniform named \"%s\"", name)
    return loc


def desenha_triangulo():
    glDrawArrays(GL_TRIANGLES, 0, 3)
    # # 1rst attribute buffer : vertices
    # glEnableVertexAttribArray(0)
    # glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer)
    # glVertexAttribPointer(
    #     0,                  # attribute 0. No particular reason for 0, but must match the layout in the shader.
    #     3,                  # tamanho
    #     GL_FLOAT,           # tipo
    #     GL_FALSE,           # normalized?
    #     0,                  # stride
    #     0                   # array buffer offset
    # )
    #
    # # Draw the triangle !
    # glDrawArrays(GL_TRIANGLES, 0, 3)  # 3 indices starting at 0 -> 1 triangle
    #
    # glDisableVertexAttribArray(0)


def define_triangulo():
    triangulo = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                 0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                 0.0, 0.5, 0.0, 0.0, 0.0, 1.0]

    tamanho = 4 * len(triangulo)

    tri, tam = triangulo, tamanho

    vbo = GLuint(0)

    glGenBuffers(1, vbo)

    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, tam, (GLfloat * len(tri))(*tri), GL_STATIC_DRAW)

    # posições
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, tam / 3, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # cores
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, tam / 3, ctypes.c_void_p((tam / 3) / 2))
    glEnableVertexAttribArray(0)


def display():

    # Limpar todos os pixels
    glClear(GL_COLOR_BUFFER_BIT)

    # # Set color variable of the fragment shader
    # glUniform3f(getUniLoc(shaderProgram, "userColor"), 0.4, 0.4, 0.8)

    if shader:
        glUseProgram(shader)

    desenha_triangulo()

    glutSwapBuffers()


def init():
    global shader

    # selecionar cor de fundo (preto)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    codigo_shader_vertices = """
    #version 460
    in layout (location = 0) vec3 position;
    in layout (location = 1) vec3 color;
    
    out vec3 newColor;
    void main()
    {
        gl_Position = vec4(position, 1.0);
        newColor = color;
    }
    """

    codigo_shader_fragments = """
    #version 460
    in vec3 newColor;
    
    out vec4 outColor;
    void main()
    {
        outColor = vec4(newColor, 1.0);
    }
    """

    # Create shader object
    shader = cria_shader(codigo_shader_vertices, codigo_shader_fragments)

    define_triangulo()

    # inicializar sistema de viz.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard(key, x, y):

    if key == b'\x1b':
        exit(0)


def idle():
    glutPostRedisplay()


if __name__ == '__main__':
    main()
