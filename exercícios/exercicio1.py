from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# vertices = (
#     (1, -1, -1),
#     (1, 1, -1),
#     (-1, 1, -1),
#     (-1, -1, -1),
#     (1, -1, 1),
#     (1, 1, 1),
#     (-1, -1, 1),
#     (-1, 1, 1)
# )
#
# arestas = (
#     (0, 1),
#     (0, 3),
#     (0, 4),
#     (2, 1),
#     (2, 3),
#     (2, 7),
#     (6, 3),
#     (6, 4),
#     (6, 7),
#     (5, 1),
#     (5, 4),
#     (5, 7),
# )

full_screen = False
window_size = (800, 600)

desenho = 1


def inicializar():
    # selecionar cor de fundo (preto)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # inicializar sistema de viz.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glOrtho(0.0, window_size[0], 0.0, window_size[1], -500.0, 500.0)

    glMatrixMode(GL_MODELVIEW)  # Select The Modelview Matrix
    glLoadIdentity()            # Inicializa com matriz identidade


def desenho1():

    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.25, 0.4, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glEnd()
    glPopMatrix()
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, -0.5, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(-0.5, 0.0, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glEnd()

    glPopMatrix()
    glFlush()

    glutPostRedisplay()


def desenho2():

    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, -0.5, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(-0.5, 0.0, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.25, 0.4, 0.0)
    glVertex3f(0.25, 0.4, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()
    glPopMatrix()
    glFlush()

    glutPostRedisplay()


def desenho3():
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, -0.5, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(-0.5, 0.0, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.25, 0.4, 0.0)
    glVertex3f(0.25, 0.4, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(-0.25, -0.4, 0.0)
    glVertex3f(-0.5, 0.0, 0.0)
    glEnd()
    glPopMatrix()
    glFlush()

    glutPostRedisplay()


def desenho4():
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(0.0, -0.5, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glEnd()
    glBegin(GL_LINES)
    glVertex3f(-0.5, 0.0, 0.0)
    glVertex3f(0.5, 0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.0, 0.1, 0.4)
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.2, 0.4, 0.0)
    glVertex3f(0.4, 0.0, 0.0)
    glVertex3f(0.2, -0.4, 0.0)
    glVertex3f(-0.2, -0.4, 0.0)
    glVertex3f(-0.4, 0.0, 0.0)
    glVertex3f(-0.2, 0.4, 0.0)
    glEnd()
    glPopMatrix()
    glFlush()

    glutPostRedisplay()


def desenhar():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    global desenho

    if desenho == 1:
        desenho1()
    elif desenho == 2:
        desenho2()
    elif desenho == 3:
        desenho3()
    elif desenho == 4:
        desenho4()

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
    global desenho

    if tecla == b'\x1b':
        exit()
    elif tecla == b'f':
        full_screen = not full_screen
        if full_screen:
            glutFullScreen()

        else:
            glutReshapeWindow(window_size[0], window_size[1])

    elif tecla == b'1':
        desenho = 1
    elif tecla == b'2':
        desenho = 2
    elif tecla == b'3':
        desenho = 3
    elif tecla == b'4':
        desenho = 4
    else:
        print(tecla)


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(window_size[0], window_size[1])
glutInitWindowPosition(100, 100)
window = glutCreateWindow("Exercicio 1")
inicializar()

glutDisplayFunc(desenhar)
glutReshapeFunc(redesenhar)
glutPassiveMotionFunc(None)
glutIdleFunc(desenhar)

glutIgnoreKeyRepeat(0)

glutKeyboardFunc(teclado_pressionar)

glutMainLoop()

