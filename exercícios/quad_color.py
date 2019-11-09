from OpenGL.GL import *
from OpenGL.GLUT import *

full_screen = False
window_size = (800, 600)


def inicializar():
    # selecionar cor de fundo (preto)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # inicializar sistema de viz.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)  # Select The Modelview Matrix
    glLoadIdentity()            # Inicializa com matriz identidade


def quad():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5, -0.5, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-0.5, 0.5, 0.0)

    glEnd()


def desenhar():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    quad()
    glLoadIdentity()
    glutSwapBuffers()


def redesenhar(w, h):
    # Guarda informações de altura e largura do modo janela
    if not full_screen:
        # talvez mudar
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


def teclado(tecla, x, y):
    global full_screen
    if tecla == b'\x1b':
        exit()
    if tecla == b'f':
        full_screen = not full_screen
        if full_screen:
            glutFullScreen()

        else:
            glutReshapeWindow(window_size[0], window_size[1])

    else:
        print(tecla)


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(window_size[0], window_size[1])
glutInitWindowPosition(200, 200)
window = glutCreateWindow("Quad Color Test")

glutDisplayFunc(desenhar)
glutReshapeFunc(redesenhar)
glutIdleFunc(desenhar)
glutKeyboardFunc(teclado)

glutMainLoop()

