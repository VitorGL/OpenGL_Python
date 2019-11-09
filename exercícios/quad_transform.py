from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

full_screen = False
window_size = (800, 800)

habilitar_menu = False
x_trans = 0
y_trans = 0
angulo = 0
escala = 1.0


def inicializar():
    # selecionar cor de fundo (preto)
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glShadeModel(GL_SMOOTH)
    # inicializar sistema de viz.
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-100, 100, -100, 100, -100, 100)

    glMatrixMode(GL_MODELVIEW)  # Seleciona a Modelview Matrix
    glLoadIdentity()            # Inicializa com matriz identidade


def desenha_eixos():
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-100.0, 0.0, 0.0)
    glVertex3f(100.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -100.0, 0.0)
    glVertex3f(0.0, 100.0, 0.0)
    glEnd()


def mostrar_menu():
    global habilitar_menu
    global x_trans
    global y_trans
    global angulo
    global escala

    print("\n=== MENU ===")
    print("\n1 - Translacao")
    print("\n2 - Rotacao")
    print("\n3 - Escala")
    print("\n4 - Sair")
    print("\nOpcao: ")

    op = int(input())

    if op == 1:
        print("\n\nInforme o vetor de translacao (entre -100.0 e 100.0)")
        x_trans = float(input("\nX : "))
        y_trans = float(input("Y : "))
        habilitar_menu = False
    elif op == 2:
        angulo = float(input("\n\nInforme o angulo de rotacao (em graus): "))
        habilitar_menu = False
    elif op == 3:
        escala = float(input("\n\nInforme o fator de escala: "))
        habilitar_menu = False
    elif op == 4:
        exit(1)
    else:
        print("\n\nOpcao invalida\n\n")


def desenhar():
    global x_trans
    global y_trans
    global angulo
    global escala

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity() # Inicializa com matriz identidade

    desenha_eixos()

    glColor3f(1.0, 0.0, 0.0)

    glPushMatrix()

    glTranslatef(x_trans, y_trans, 0.0)
    glRotatef(angulo, 0.0, 0.0, 1.0)
    glScalef(escala, escala, escala)
    glutWireCube(10)

    glPopMatrix()

    glutSwapBuffers()
    glutPostRedisplay()

    if habilitar_menu:
        mostrar_menu()


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


def mouse(botao, estado, x, y):
    global habilitar_menu

    # if botao == GLUT_LEFT_BUTTON:
    #     if estado == GLUT_DOWN:
    #         habilitar_menu = True
    # else:
    #     print(botao)
    #     print(estado)


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(window_size[0], window_size[1])
glutInitWindowPosition(100, 100)
window = glutCreateWindow("Exercicio 3")
inicializar()

glutDisplayFunc(desenhar)
# glutReshapeFunc(redesenhar) # O PROBLEMA ESTAVA AQUI
# glutPassiveMotionFunc(None)
glutIdleFunc(desenhar)

# glutIgnoreKeyRepeat(0)

glutKeyboardFunc(teclado_pressionar)
glutMouseFunc(mouse)

glutMainLoop()

