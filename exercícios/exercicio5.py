from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

#
# FALTANDO COISA
#

fps_desejado = 60
var = 0.0
direcao = 1.0
# fpsViewer = glcFPSViewer("Triangle Animation. ", " - Press ESC to Exit")


def idle():
    global var
    global direcao
    global fps_desejado

    ultimo_t = 0.0

    # Get elapsed time
    tempo = glutGet(GLUT_ELAPSED_TIME)
    # convert milliseconds to seconds
    tempo /= 1000.0

    # Calculate frame time
    tempo_de_frame = tempo - ultimo_t
    # Calculate desired frame time
    tempo_fps_desejado = 1.0 / fps_desejado

    # Check if the desired frame time was achieved. If not, skip animation.
    if tempo_de_frame <= tempo_fps_desejado:
        return

    # UPDATE ANIMATION VARIABLES
    if var <= -0.001 or var >= 1.0:
        direcao *= -1

    var += direcao*0.005

    # Update ultimo_t for next time, using static local variable
    ultimo_t = tempo

    glutPostRedisplay()


# Mouse callback
def mouse(botao, estado, x, y):
    if botao == GLUT_LEFT_BUTTON and estado == GLUT_DOWN:
        pass


def desenhar():

    # Limpar todos os pixels
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_POLYGON)
    glVertex2f(0.0, 0.0)
    glVertex2f(1.0, 0.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(0.0, var)
    glEnd()

    glutSwapBuffers()

    # Print FPS
    # fpsViewer->drawFPS()


def inicializar():

    # selecionar cor de fundo (preto)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # inicializar sistema de viz.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard(tecla, x, y):
    global fps_desejado

    if tecla == b'1':
        fps_desejado = 60
    elif tecla == b'2':
        fps_desejado = 30
    elif tecla == b'3':
        fps_desejado = 10
    elif tecla == b'\x1b':
        exit(0)

    else:
        print(tecla)


glutInit()

print("Triangle Animation Example")
print("--------------------------")
print("Press 1 to change FPS to ~60")
print("Press 2 to change FPS to ~30")
print("Press 3 to change FPS to ~10")
print("Press ESC to exit")

glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGB)
glutInitWindowSize(400, 400)
glutCreateWindow("Exercicio 5")
glutMouseFunc(mouse)
glutKeyboardFunc(keyboard)
glutIdleFunc(idle)
inicializar()
glutDisplayFunc(desenhar)
glutMainLoop()



