from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

full_screen = False
window_size = (800, 600)

qtd_pontos = 6


def inicializar():
    # selecionar cor de fundo (preto)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # inicializar sistema de viz.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10.0, 390, -2, 2, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)  # Select The Modelview Matrix
    glLoadIdentity()            # Inicializa com matriz identidade


def desenho(pontos):

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_STRIP)
    # h = (2*math.pi)/pontos
    glVertex3f(0, 0, 0.0)

    for x in range(361)[::int(360/pontos)]:
        y = math.sin(x * (math.pi / 180))
        glVertex3f(x, y, 0.0)
        # print(x, y)

    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(-10, 0.0, 0.0)
    glVertex3f(390, 0.0, 0.0)
    glEnd()

    glFlush()

    glutPostRedisplay()


def desenhar():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    global qtd_pontos

    desenho(qtd_pontos)

    glLoadIdentity()
    glutSwapBuffers()
    glutPostRedisplay()


def redesenhar(w, h):
    # Guarda informações de altura e largura do modo janela
    if not full_screen:
        width = w
        height = h

    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if w <= h:
        glOrtho(-1, 1, -1 * h / w, 1 * h / w, -10.0, 10.0)
    else:
        glOrtho(-1 * w / h, 1 * w / h, -1, 1, -10.0, 10.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


def teclado_pressionar(tecla, x, y):
    global full_screen
    global qtd_pontos

    if tecla == b'\x1b':
        exit()
    elif tecla == b'f':
        full_screen = not full_screen
        if full_screen:
            glutFullScreen()

        else:
            glutReshapeWindow(window_size[0], window_size[1])
    elif tecla == b'a':
        qtd_pontos = 6
    elif tecla == b'b':
        qtd_pontos = 12
    elif tecla == b'c':
        qtd_pontos = 180
    else:
        print(tecla)


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(window_size[0], window_size[1])
glutInitWindowPosition(100, 100)
window = glutCreateWindow("Exercicio 2")
inicializar()

glutDisplayFunc(desenhar)
# glutReshapeFunc(redesenhar) # O PROBLEMA ESTAVA AQUI
glutPassiveMotionFunc(None)
glutIdleFunc(desenhar)

glutIgnoreKeyRepeat(0)

glutKeyboardFunc(teclado_pressionar)

glutMainLoop()

