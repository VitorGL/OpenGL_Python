# # coding=utf-8
# from __future__ import unicode_literals
# from OpenGL.GL import *
# from OpenGL.GLU import *
# from OpenGL.GLUT import *
# from OpenGL import *
# from random import uniform
# import numpy as np
# import PIL.Image as img
#
# COLOR_RUBY = 1
# COLOR_DEFAULT = 2
#
#
# # Aqui é criada a referência ao objeto que gerenciará as texturas
# textureManager = None
# selected = 0
# object = 1
#
# width = None
# height = None
#
# zoom = 1.8
# pan = [0.0, 0.0]
# fullScreen = False
# rotationX = 0.0
# rotationY = 0.0
# last_x = None
# last_y = None
#
# wrappingMode = 1
# magMode = 1
# minMode = 1
# colorMode = 0
# tiles = 1.0
# numberOfTextures = 0
#
# # Usado no colorMode = GL_MODULATE
#
#
# def setMaterial(op):
#     if op == COLOR_RUBY:
#
#         # Material do objeto (neste caso, ruby)
#         objeto_ambient = [ 0.2, 0.0, 0.0, 1.0 ]
#         objeto_difusa = [ 0.6, 0.0, 0.0, 1.0 ]
#         objeto_especular = [ 0.7, 0.6, 0.6, 1.0 ]
#         objeto_brilho = [ 90.0]
#
#         glMaterialfv(GL_FRONT, GL_AMBIENT, objeto_ambient)
#         glMaterialfv(GL_FRONT, GL_DIFFUSE, objeto_difusa)
#         glMaterialfv(GL_FRONT, GL_SPECULAR, objeto_especular)
#         glMaterialfv(GL_FRONT, GL_SHININESS, objeto_brilho)
#
#     if op == COLOR_DEFAULT:
#
#         # Set colors to the default (according to https:#www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glMaterial.xml)
#         objeto_ambient = [0.2, 0.2, 0.2, 1.0]
#         objeto_difusa = [0.8, 0.8, 0.8, 1.0]
#         objeto_especular = [0.0, 0.0, 0.0, 1.0]
#
#         glMaterialfv(GL_FRONT, GL_AMBIENT, objeto_ambient)
#         glMaterialfv(GL_FRONT, GL_DIFFUSE, objeto_difusa)
#         glMaterialfv(GL_FRONT, GL_SPECULAR, objeto_especular)
#
#
# # Como as imagens são lidas a partir do canto superior direito, temos que inverter as coordenadas 'u' e 'v'
#
# def display():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluPerspective(60, width/height, 0.1, 100)
#
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
#
#     gluLookAt(pan[0], pan[1], zoom, pan[0], pan[1], 0.0, 0.0, 1.0, 0.0)
#     # Seleciona a textura corrente
#     glBindTexture(selected)
#     # aspectRatio = textureManager->GetAspectRatio(selected)
#     #
#     # # Calculo abaixo funciona apenas se textura estiver centralizada na origem
#     # h = 1.0
#     # w = 1.0
#     #
#     # if aspectRatio > 1.0:
#     #     h  = h/aspectRatio
#     # else :
#     #     w  = w*aspectRatio
#     h = 1.0
#     w = 1.0
#
#     glPushMatrix()
#     glRotatef(rotationY, 0.0, 1.0, 0.0)
#     glRotatef(rotationX, 1.0, 0.0, 0.0)
#
#     if object == 1:
#         glBegin(GL_QUADS)
#         glNormal3f(0.0, 0.0, 1.0)
#         glTexCoord2f(0.0, 0.0)
#         glVertex3f(-w, -h, 0.0)
#
#         glTexCoord2f(tiles, 0.0)
#         glVertex3f(w, -h, 0.0)
#
#         glTexCoord2f(tiles, tiles)
#         glVertex3f(w, h, 0.0)
#
#         glTexCoord2f(0.0, tiles)
#         glVertex3f(-w, h, 0.0)
#
#         glEnd()
#
#     else:
#         # object == 2
#
#         glPushMatrix()
#         glRotatef(30, 1.0, 0.0, 0.0)  # Put the teapot in a better position
#         glutSolidTeapot(0.7)
#         glPopMatrix()
#
#     glPopMatrix()
#
#     glutSwapBuffers()
#
#     # Desabilita o uso de texturas
#     glDisable(GL_TEXTURE_2D)
#
#
# def resizeWindow(w, h):
#
#     width = w
#     height = h
#     glViewport(0, 0, w, h)
#
#
# def changeWindowTitle(name):
#
#     glutSetWindow(window)  # Set main window as current
#     glutSetWindowTitle(name)  # change title
#
#
# def keyboard(key, x, y):
#     global zoom
#     global minMode
#     global wrappingMode
#     global tiles
#     global selected
#     global numberOfTextures
#
#     if type(key) == int():
#
#         val = int(key)
#         if 0 < val <= numberOfTextures:
#             selected = val-1
#
#     if key == 27:
#         exit(0)
#     elif key == '+':
#         if zoom >= 0.3:
#             zoom -= 0.1
#     elif key == '-':
#         if zoom <= 20.0:
#             zoom += 0.1
#     elif key == 'w':
#         # wrapping modes
#         wrappingMode = not wrappingMode
#         if wrappingMode:
#             glTexParameterf(GL_REPEAT)
#             changeWindowTitle("Wrapping Mode = GL_REPEAT")
#         else:
#             glTexParameterf(GL_CLAMP)
#             changeWindowTitle("Wrapping Mode = GL_CLAMP")
#
#         # textureManager->Update()
#     elif key == 'm':  # minificação
#         minMode = not minMode
#
#         if minMode:
#             glTextureParameterf(GL_LINEAR)
#             changeWindowTitle("Minification Mode = GL_LINEAR")
#         else:
#             glTextureParameterf(GL_NEAREST)
#             changeWindowTitle("Minification Mode = GL_NEAREST")
#
#         # textureManager->Update()
#     # elif key == 'g':  # magnificação
#     #     magMode = not magMode
#     #     if magMode:
#     #         textureManager->SetMagFilterMode(GL_NEAREST)
#     #
#     #         changeWindowTitle("Magnification Mode = GL_NEAREST")
#     #     else:
#     #         textureManager->SetMagFilterMode(GL_LINEAR)
#     #         changeWindowTitle("Magnification Mode = GL_LINEAR")
#     #
#     #     textureManager->Update()
#     #
#     # elif key == 'c':  # Color Mode
#     #     colorMode += 1
#     #     if colorMode > 3:
#     #         colorMode = 0
#     #     if colorMode == 0:
#     #         setMaterial(COLOR_DEFAULT)
#     #         textureManager->SetColorMode(GL_MODULATE)
#     #         changeWindowTitle("Color Mode = GL_MODULATE (Default color)")
#     #
#     #     elif colorMode == 1:
#     #         setMaterial(COLOR_RUBY)
#     #         textureManager->SetColorMode(GL_MODULATE)
#     #         changeWindowTitle("Color Mode = GL_MODULATE (Ruby color)")
#     #
#     #     elif colorMode == 2:
#     #         textureManager->SetColorMode(GL_REPLACE)
#     #         changeWindowTitle("Color Mode = GL_REPLACE")
#     #
#     #     elif colorMode == 3:
#     #         env_color =[ 0.2, 0.8, 0.0, 1.0 ]
#     #         setMaterial(COLOR_DEFAULT)
#     #         textureManager->SetEnvColor(env_color)
#     #         textureManager->SetColorMode(GL_BLEND)
#     #         changeWindowTitle("Color Mode = GL_BLEND")
#     #
#     #     textureManager->Update()
#
#     elif key == 't':  # Increase Texture Tiles
#         tiles += 1
#
#     elif key == 'T':  # Decrease Texture Tiles
#         if tiles > 1.0:
#             tiles -= 1
#
#     glutPostRedisplay()
#
#
# def specialKeys(key, x, y):
#     global fullScreen
#
#     f = 0.05
#     if key == GLUT_KEY_UP:
#         pan[1]+=f
#
#     elif key == GLUT_KEY_DOWN:
#         pan[1]-=f
#
#     elif key == GLUT_KEY_LEFT:
#         pan[0]-=f
#
#     elif key == GLUT_KEY_RIGHT:
#         pan[0]+=f
#
#     elif key == GLUT_KEY_F11:
#         if not fullScreen:
#             glutFullScreen()
#         else:
#             glutReshapeWindow(800, 600)
#
#         fullScreen = not fullScreen
#
#     elif key == GLUT_KEY_F1:
#         object = 1
#
#     elif key == GLUT_KEY_F2:
#         object = 2
#
#     glutPostRedisplay()
#
#
# def init():
#     global numberOfTextures
#
#     glClearColor (0.5, 0.5, 0.5, 0.0)
#     glShadeModel (GL_SMOOTH)
#     glEnable(GL_DEPTH_TEST)               # Habilita Z-buffer
#     glEnable(GL_LIGHTING)                 # Habilita luz
#     glEnable(GL_LIGHT0)                   # habilita luz 0
#
#     glEnable(GL_ALPHA_TEST)      # O alpha test descarta fragmentos dependendo de uma comparação (abaixo)
#     glAlphaFunc(GL_GREATER, 0.1) # Info: https:#www.opengl.org/sdk/docs/man2/xhtml/glAlphaFunc.xml
#
#     glEnable(GL_BLEND)
#     glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) # https:#www.opengl.org/sdk/docs/man/html/glBlendFunc.xhtml
#
#     # Cor da fonte de luz (RGBA)
#     cor_luz = [1.0, 1.0, 1.0, 1.0]
#     posicao_luz = [0.0, 0.0, 10.0, 1.0]
#
#     # Define parametros da luz
#     glLightfv(GL_LIGHT0, GL_AMBIENT, cor_luz)
#     glLightfv(GL_LIGHT0, GL_DIFFUSE, cor_luz)
#     glLightfv(GL_LIGHT0, GL_SPECULAR, cor_luz)
#     glLightfv(GL_LIGHT0, GL_POSITION, posicao_luz)
#
#     # Essa é a principal parte deste exemplo
#     # textureManager = glcTex            # Criação do arquivo que irá gerenciar as texturas
#     numberOfTextures = 4       # Estabelece o número de texturas que será utilizado
#     glCreateTextures(GL_TEXTURE_2D, 4, ["verde.png", "azul.png", "vermelho.png", "grao_de_fumaca.png"])
#     # Para testar magnificação, usar a imagem marble128
#     # Textura transparente, não sendo múltipla de zero
#     # Textura transparente, não sendo múltipla de zero
#
#
# # Motion callback#glcTexture *texture
# def motion(x, y):
#     global rotationX
#     global rotationY
#     global last_x
#     global last_y
#
#     rotationX += (y - last_y)
#     rotationY += (x - last_x)
#
#     last_x = x
#     last_y = y
#
#
# # Mouse callback
# def mouse(button, state, x, y):
#     global zoom
#
#     if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
#         last_x = x
#         last_y = y
#
#     if button == 3: # Scroll up
#         if zoom >= 0.3:
#             zoom -= 0.04
#
#     if button==4:  # Scroll down
#         if zoom <= 20.0:
#             zoom += 0.04
#
#
# def idle():
#     glutPostRedisplay()
#
#
# def printOpenGLVersion():
#
#     print("\nDados do OpenGL instalado neste sistema operacional:")
#     vendor = glGetString(GL_VENDOR)
#     version = glGetString(GL_VERSION)
#     render = glGetString(GL_RENDERER)
#     print("   Vendor:   ", vendor)
#     print("   Version:  ", version)
#     print("   Renderer: ", render)
#     if version[0] == '1':
#
#         print("\nAviso: A biblioteca pode nao funcionar corretamente (versao antiga do OpenGL).")
#         print("\n       Maiores detalhes nas notas do arquivo \"README_FIRST.txt\".\n")
#
#     print()
#
#
# glutInit()
# glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
# glutInitWindowSize(1024, 768)
# glutInitWindowPosition(100, 100)
# window = glutCreateWindow("Title")
#
# init()
# printOpenGLVersion()
# print("\n------------------------------------------------------------\n")
# print("Instrucoes: ")
# print(" * Modifique as texturas pressionando as teclas de um 1 a ", numberOfTextures)
# print(" * Pressione F1 e F2 para mudar os objetos")
# print(" * Teclas '+' e '-' fazem zoom")
# print(" * Teclas 'w' para alternar entre os \"Wrapping modes\"")
# print(" * Teclas 'm' para alternar entre os modos do filtro de minificação")
# print(" * Teclas 'g' para alternar entre os modos do filtro de magnificação")
# print(" * Teclas 'c' para alternar entre os modos de cor de textura")
# print(" * Teclas 't' ou 'T' para aumentar/diminuir o tamanho da coordenada de textura (em 2D)")
# print(" * Direcionais do teclado movem a camera (pan)")
# print(" * Mouse rotaciona o objeto")
# print(" * Pressione F11 para ligar e desligar modo FullScreen")
#
# glutDisplayFunc(display)
# glutReshapeFunc(resizeWindow)
# glutKeyboardFunc(keyboard)
# glutSpecialFunc( specialKeys )
# glutMouseFunc( mouse )
# glutMotionFunc( motion )
# glutIdleFunc(idle)
# glutMainLoop()
#

# coding=utf-8
import OpenGL.GL.shaders
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy
from PIL import Image
import math

texid = None
tam = 2
fAspect = None
vertices = [(-(tam/2), -(tam / 2), 0),
            ((tam / 2), -(tam / 2), 0),
            ((tam / 2), (tam / 2), 0),
            (-(tam / 2), (tam / 2), 0)
            ]


def carregar_textura():
    image = Image.open("vermelho.png")
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = flipped_image.convert("RGBA").tobytes()

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid


def draw_cube(lines=False):

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0,  0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0,  0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0,  0)
    glTexCoord2f(0.0, 1.0)
    glColor4f(0, 0, 0, 1)
    glVertex3f(-1.0,  1.0,  0)
    glEnd()


def inicializar():
    global texid
    glClearColor(0.0, 0.0, 0.0, 0.0)
    carregar_textura()

    gluPerspective(45, 800 / 600, 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glShadeModel(GL_SMOOTH)
    #
    # glEnable(GL_LIGHT0)  # habilita luz 0
    glEnable(GL_COLOR_MATERIAL)  # Utiliza cor do objeto como material
    glColorMaterial(GL_FRONT, GL_DIFFUSE)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    #
    glEnable(GL_BLEND)
    # glEnable(GL_LIGHTING)  # Habilita luz
    glEnable(GL_DEPTH_TEST)  # Habilita Z - buffer
    glEnable(GL_CULL_FACE)  # Habilita Backface - Culling

    # # #        positions                 colors        texture coords
    # # quad = [-(tam/2), -(tam / 2), 0,  1.0, 0.0, 0.0,  0.0, 0.0,
    # #         (tam / 2), -(tam / 2), 0,  0.0, 1.0, 0.0,  1.0, 0.0,
    # #         (tam / 2), (tam / 2), 0,  0.0, 0.0, 1.0,  1.0, 1.0,
    # #         -(tam / 2), (tam / 2), 0,  1.0, 1.0, 1.0,  0.0, 1.0]
    # #
    # # quad = numpy.array(quad, dtype=numpy.float32)
    # #
    # # indices = [0, 1, 2,
    # #            2, 3, 0]
    #
    # image = Image.open("vermelho.png")
    # # img_data = numpy.array(list(image.getdata()), numpy.uint8)
    # flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    # img_data = flipped_image.convert("RGBA").tobytes()
    # glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    # # print(image.width, image.height)
    # # textureSurface = pygame.image.load('test_image.png')
    # # textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    # width = image.width
    # height = image.height
    #
    # glEnable(GL_TEXTURE_2D)
    # texid = glGenTextures(1)
    #
    # glBindTexture(GL_TEXTURE_2D, texid)
    # glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
    #              0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    #
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)


def definir_visualizacao():
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    # Especifica a projeção perspectiva(angulo, aspecto, zMin, zMax)
    gluPerspective(60, fAspect, 1.0, 200)

    # posicionaObservador()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0.0, 1.0, 0.0)


def exibir():
    global texid
    global vertices

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_cube(lines=False)

    # definir_visualizacao()

    # glBegin(GL_QUADS)
    # for v in vertices:
    #     glVertex3f(v[0], v[1], v[2])
    # glEnd()

    # pontos = 40
    #
    # glColor3f(1.0, 0.0, 0.0)
    # glBegin(GL_POLYGON)
    # # h = (2*math.pi)/pontos
    # glVertex3f(0, 0, 0.0)
    #
    # for x in range(361)[::int(360 / pontos)]:
    #     y = x * (math.pi / 180)
    #     glVertex3f(1*math.cos(y), 1*math.sin(y), 0.0)
    #
    # glEnd()
    #
    # glDisable(GL_TEXTURE_2D)
    glutSwapBuffers()


def main():
    global fAspect

    largura = 800
    altura = 600
    fAspect = largura / altura
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(int(largura), int(altura))
    glutInitWindowPosition(20, 20)
    glutCreateWindow("Caverna")
    inicializar()
    glutDisplayFunc(exibir)
    # glutReshapeFunc(reformatar)
    # glutMouseFunc(mouse)
    # glutKeyboardFunc(teclado_pressionar)
    # glutSpecialFunc(teclas_especiais_press)
    # glutSpecialUpFunc(teclas_especiais_soltar)
    # glutMotionFunc(motion)
    # glutIdleFunc(idle)
    glutMainLoop()


if __name__ == "__main__":
    main()