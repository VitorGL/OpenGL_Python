# coding=utf-8
from __future__ import unicode_literals
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import uniform
from PIL import Image
import numpy as np
import math

# Janela
altura = 400
largura = 800

# Mouse
x_velho = 0
y_velho = 0
x_novo = 0
y_novo = 0

# Camera
camera_x = 0
camera_y = 0
camera_z = 45
rot_camera = False
rot_x = 25
rot_y = 0
angulo = 60
fAspect = largura/altura

visao_x = 0
visao_y = 0
visao_z = 0


def desenha_circulo(tam, alpha):
    pontos = 40

    glBegin(GL_POLYGON)
    # h = (2*math.pi)/pontos
    glVertex3f(0, 0, 0.0)

    for x in range(361)[::int(360 / pontos)]:
        y = x * (math.pi / 180)
        glVertex3f(tam * math.cos(y), tam * math.sin(y), 0.0)

    glEnd()
    glPushMatrix()
    glColor4f(0.8, 0.8, 0.8, alpha - 0.1)
    pontos = 40
    glScalef(1.3, 1.3, 1)
    glBegin(GL_POLYGON)
    # h = (2*math.pi)/pontos
    glVertex3f(0, 0, 0.0)

    for x in range(361)[::int(360 / pontos)]:
        y = x * (math.pi / 180)
        glVertex3f(tam * math.cos(y), tam * math.sin(y), 0.0)

    glEnd()
    glPopMatrix()


def desenha_quadrado(tam):
    glBegin(GL_QUADS)
    # glColor4f(0, 0, 0, 1)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-(tam/2), -(tam/2), 0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f((tam/2), -(tam/2), 0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f((tam/2), (tam/2), 0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-(tam/2), (tam/2), 0)
    glEnd()


class Particulas():
    def __init__(self, x=0, y=0, z=0,
                 velocidade_x=None,
                 velocidade_y=None,
                 velocidade_z=None,
                 tam=2
                 ):
        self.tam = tam
        self.x = x
        self.y = y
        self.z = z
        if (velocidade_x, velocidade_y, velocidade_z) == (None, None, None):
            self.velocidade_x = uniform(-1.0, 1.0)
            self.velocidade_y = uniform(1.0, 3.0)
            self.velocidade_z = uniform(-1.0, 1.0)
        self.alpha = 1

    def mostrar(self):
        glPushMatrix()
        glColor4f(0.8, 0.8, 0.8, self.alpha)
        glTranslatef(self.x, self.y, self.z)
        # glRectf(-(self.tam/2), -(self.tam/2), (self.tam/2), (self.tam/2))
        desenha_quadrado(self.tam)
        glPopMatrix()

    def atualizar(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y
        self.z += self.velocidade_z
        self.alpha -= 0.05
        self.tam += 0.2

    def morte(self):
        return self.alpha <= 0


particulas = []


# Funções

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


# Inicializa opengl
def inicializar():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    carregar_textura()

    glShadeModel(GL_SMOOTH)

    # glEnable(GL_LIGHT0)  # habilita luz 0
    glEnable(GL_COLOR_MATERIAL)  # Utiliza cor do objeto como material
    glColorMaterial(GL_FRONT, GL_DIFFUSE)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glEnable(GL_BLEND)
    # glEnable(GL_LIGHTING)  # Habilita luz
    glEnable(GL_DEPTH_TEST)  # Habilita Z - buffer
    glEnable(GL_CULL_FACE)  # Habilita Backface - Culling


def idle():
    glutPostRedisplay()


def desenha_objetos():
    global particulas

    pa = Particulas(0, -10, 0)
    particulas.append(pa)
    for part in particulas:
        part.atualizar()
        part.mostrar()
        if part.morte():
            particulas.remove(part)


#############################
# Glut and image functions
def exibir():
    global rot_x
    global rot_y

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    definir_visualizacao()

    desenha_objetos()

    glutSwapBuffers()


def reformatar(larg, alt):
    largura = larg
    altura = alt
    glViewport(0, 0, larg, alt)


def definir_visualizacao():
    global camera_x
    global camera_y
    global camera_z
    global visao_x
    global visao_y
    global visao_z
    global angulo
    global fAspect

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    # Especifica a projeção perspectiva(angulo, aspecto, zMin, zMax)
    gluPerspective(angulo, fAspect, 1.0, 200)

    # posicionaObservador()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(camera_x, camera_y, camera_z, visao_x, visao_y, visao_z, 0.0, 1.0, 0.0)


def teclado_pressionar(tecla, x, y):
    global camera_x
    global camera_y
    global camera_z
    global visao_x
    global visao_y
    global visao_z

    if tecla == b'\x1b':
        exit(0)
    elif tecla == b'w':
        camera_y += 1
        visao_y += 1
    elif tecla == b'a':
        camera_x -= 1
        visao_x -= 1
    elif tecla == b's':
        camera_y -= 1
        visao_y -= 1
    elif tecla == b'd':
        camera_x += 1
        visao_x += 1

    else:
        print(tecla)

    glutPostRedisplay()


def teclado_soltar(tecla, x, y):

    if tecla == b'\x1b':
        exit(0)
    else:
        print(tecla)

    glutPostRedisplay()


def teclas_especiais_press(tecla, x, y):
    global rot_camera

    if tecla == 112:
        rot_camera = True
    else:
        print(tecla)

    glutPostRedisplay()


def teclas_especiais_soltar(tecla, x, y):
    global rot_camera

    if tecla == 112:
        rot_camera = False
    else:
        print(tecla)

    glutPostRedisplay()


def mouse(botao, estado, x, y):
    global x_velho
    global y_velho
    global x_novo
    global y_novo
    global rot_camera

    angulo = 0

    if botao == GLUT_LEFT_BUTTON:
        if estado == GLUT_DOWN:
            print("mouse x:", x, "\nmouse y:", y)
            x_velho = x
            y_velho = y
        elif estado == GLUT_UP:
            if not rot_camera:
                print("mova")
            else:
                print("rotacione")

            # print("mouse x:", x, "\nmouse y:", y)
            # print("dif x:", (x - x_velho), "\ndif y:", (y - y_velho))

    else:
        print(botao)
        print(estado)

    # get mouse coordinates from Windows
    # mouseX = LOWORD(lParam)


    # these lines limit the camera's range

    if (x - x_velho) > 0:  # mouse moved to the right
        angulo += 3.0
    elif (x - x_velho) < 0:  # mouse moved to the left
        angulo -= 3.0


# Motion callback
def motion(x, y):
    global x_velho
    global y_velho
    global rot_x
    global rot_y

    rot_x += (y - y_velho)
    rot_y += (x - x_velho)
    print(x, y)

    x_velho = x
    y_velho = y


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(int(largura), int(altura))
glutInitWindowPosition(20, 20)
glutCreateWindow("Caverna")
inicializar()
glutDisplayFunc(exibir)
glutReshapeFunc(reformatar)
glutMouseFunc(mouse)
glutKeyboardFunc(teclado_pressionar)
glutSpecialFunc(teclas_especiais_press)
glutSpecialUpFunc(teclas_especiais_soltar)
glutMotionFunc(motion)
glutIdleFunc(idle)
glutMainLoop()