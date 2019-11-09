from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# FALTANDO COISA

x_trans_peca = -2.5
y_trans_peca = -2.5


def idle():
    pass
    # global var
    # global direcao
    # global fps_desejado
    #
    # ultimo_t = 0.0
    #
    # # Get elapsed time
    # tempo = glutGet(GLUT_ELAPSED_TIME)
    # # convert milliseconds to seconds
    # tempo /= 1000.0
    #
    # # Calculate frame time
    # tempo_de_frame = tempo - ultimo_t
    # # Calculate desired frame time
    # tempo_fps_desejado = 1.0 / fps_desejado
    #
    # # Check if the desired frame time was achieved. If not, skip animation.
    # if tempo_de_frame <= tempo_fps_desejado:
    #     return
    #
    # # UPDATE ANIMATION VARIABLES
    # if var <= -0.001 or var >= 1.0:
    #     direcao *= -1
    #
    # var += direcao*0.005
    #
    # # Update ultimo_t for next time, using static local variable
    # ultimo_t = tempo
    #
    # glutPostRedisplay()


# Mouse callback
def mouse(botao, estado, x, y):
    global x_trans_peca
    global y_trans_peca

    if botao == GLUT_LEFT_BUTTON and estado == GLUT_DOWN:
        if x < 150:
            x_trans_peca = -int(x / 100) - 0.5
            print(int(x / 100.0))
            print("negativo")
        else:
            x_trans_peca = int(x / 100) - 0.5
            print(int(x / 100.0))
            print("positivo")

        # print(x)

        if y < 150:
            y_trans_peca = int(y / 100) - 0.5
            print((y / 3))
            print("positivo")
        else:
            y_trans_peca = -int(y / 100) - 0.5
            print((y / 3))
            print("negativo")
        # print(y)
        print()


def desenhar():
    global x_trans_peca
    global y_trans_peca

    # Limpar todos os pixels
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    for i in range(-3, 3)[::2]:
        for j in range(-3, 3)[::2]:
            glBegin(GL_POLYGON)
            glVertex2f(i, j)
            glVertex2f(i, j+1)
            # glColor3f(1.0, 1.0, 0.0)
            glVertex2f(i+1, j+1)
            glVertex2f(i+1, j)
            glEnd()

    for i in range(-2, 3)[::2]:
        for j in range(-2, 3)[::2]:
            # glColor3f(1.0, 0.0, 0.0)
            glBegin(GL_POLYGON)
            glVertex2f(i, j)
            glVertex2f(i, j+1)
            # glColor3f(1.0, 1.0, 0.0)
            glVertex2f(i+1, j+1)
            glVertex2f(i+1, j)
            glEnd()

    glPopMatrix()

    glPushMatrix()
    glTranslatef(x_trans_peca, y_trans_peca, 0)
    glColor3f(1.0, 0.0, 0.0)
    glutSolidSphere(0.5, 50, 50)
    glPopMatrix()

    glLoadIdentity()
    glutSwapBuffers()
    glutPostRedisplay()

    # Print FPS
    # fpsViewer->drawFPS()


def inicializar():

    # selecionar cor de fundo (preto)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # inicializar sistema de viz.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3.0, 3.0, -3.0, 3.0, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def keyboard(tecla, x, y):

    if tecla == b'\x1b':
        exit(0)
    else:
        print(tecla)


glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGB)
glutInitWindowSize(300, 300)
glutCreateWindow("Exercicio 6")
glutMouseFunc(mouse)
glutKeyboardFunc(keyboard)
glutIdleFunc(idle)
inicializar()
glutDisplayFunc(desenhar)
glutMainLoop()



