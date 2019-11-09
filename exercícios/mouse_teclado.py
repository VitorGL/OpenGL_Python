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

motion_passiva = False

object_pos_x = window_size[0]/2
object_pos_y = window_size[1]/2
object_raio = 50

velocidade = 3
move_x = 0
move_y = 0


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


def bola():
    global object_pos_x
    global object_pos_y
    global move_x
    global move_y
    global object_raio

    # glBegin(GL_LINES)
    #
    # for aresta in arestas:
    #     for vertice in aresta:
    #         glVertex3fv(vertices[vertice])
    # glEnd()

    # Change object position if some key is pressed
    object_pos_x += move_x
    object_pos_y += move_y

    glPushMatrix()
    glColor3f(1.0, 1.0, 0.0)
    glTranslatef(object_pos_x, object_pos_y, 0.0)
    glutWireSphere(object_raio, 10, 10)
    glPopMatrix()
    glFlush()

    glutPostRedisplay()


def desenhar():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    global object_pos_x
    global object_pos_y
    global move_x
    global move_y
    global object_raio

    # Change object position if some key is pressed
    object_pos_x += move_x
    object_pos_y += move_y

    bola()

    # glLoadIdentity()
    glutSwapBuffers()
    glutPostRedisplay()


# def redesenhar(w, h):
#     # Guarda informações de altura e largura do modo janela
#     if not full_screen:
#         width = w
#         height = h
#
#     glViewport(0, 0, w, h)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#
#     if w <= h:
#         glOrtho(-1, 1, -1 * h / w, 1 * h / w, -10.0, 10.0)
#     else:
#         glOrtho(-1 * w / h, 1 * w / h, -1, 1, -10.0, 10.0)
#
#         glMatrixMode(GL_MODELVIEW)
#         glLoadIdentity()


def motion(x, y):
    global object_pos_x
    global object_pos_y

    # Inverte mouse para que origem fique no canto inferior esquerdo da janela
    # (por default, a origem é no canto superior esquerdo)
    y = window_size[1] - y

    object_pos_x = x
    object_pos_y = y


def teclado_pressionar(tecla, x, y):
    global full_screen
    global object_raio
    global motion_passiva
    global move_x
    global move_y

    if tecla == b'\x1b':
        exit()
    elif tecla == b'f':
        full_screen = not full_screen
        if full_screen:
            glutFullScreen()

        else:
            glutReshapeWindow(window_size[0], window_size[1])

    elif tecla == b'+':
        if object_raio <= 100:
            object_raio += 1

        else:
            print("\nRaio máximo atingido", object_raio)
    elif tecla == b'-':
        if object_raio > 10:
            print("\nDiminuindo raio da esfera", object_raio)
            object_raio -= 1
        else:
            print("\nRaio mínimo atingido", object_raio)
    elif tecla == b'w':
        move_y = velocidade
    elif tecla == b's':
        move_y = -velocidade
    elif tecla == b'd':
        move_x = velocidade
    elif tecla == b'a':
        move_x = -velocidade
    elif tecla == b'm':
        motion_passiva = not motion_passiva

        if motion_passiva:
            print("\n\"Passive Motion LIGADO")
            glutPassiveMotionFunc(motion)

        else:
            print("\n\"Passive Motion DESLIGADO")
            glutPassiveMotionFunc(None)
    else:
        print(tecla)


def teclado_soltar(tecla, x, y):
    global move_x
    global move_y

    if tecla == b'w' or tecla == b's':
        move_y = 0

    if tecla == b'd' or tecla == b'a':
        move_x = 0


def teclas_especiais_pressionar(tecla, x, y):
    global move_x
    global move_y

    if tecla == GLUT_KEY_UP:
        move_y = velocidade
    elif tecla == GLUT_KEY_DOWN:
        move_y = -velocidade
    elif tecla == GLUT_KEY_RIGHT:
        move_x = velocidade
    elif tecla == GLUT_KEY_LEFT:
        move_x = -velocidade
    else:
        print(tecla)


def teclas_especiais_soltar(tecla, x, y):
    global move_x
    global move_y

    if tecla == GLUT_KEY_UP or tecla == GLUT_KEY_DOWN:
        move_y = 0

    if tecla == GLUT_KEY_RIGHT or tecla == GLUT_KEY_LEFT:
        move_x = 0


def mouse(botao, estado, x, y):
    global object_pos_x
    global object_pos_y

    y = window_size[1] - y

    if botao == GLUT_LEFT_BUTTON:
        if estado == GLUT_DOWN:
            print("\nBotao esquerdo pressionado na posicao [{}, {}].".format(x, y))

            object_pos_x = x
            object_pos_y = y

        else:
            print("\nBotao esquerdo solto na posicao [{}, {}].".format(x, y)) # GLUT_UP

    if botao == GLUT_RIGHT_BUTTON:
        print("\nBotao direito do mouse pressionado.")

    if botao == 3:  # Scroll up
        print("\nScroll up.")

    if botao == 4:  # Scroll Down
        print("\nScroll down.")

    else:
        print(botao)


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(window_size[0], window_size[1])
glutInitWindowPosition(100, 100)
window = glutCreateWindow("Teste de mouse e teclado")
inicializar()

glutDisplayFunc(desenhar)
# glutReshapeFunc(redesenhar)
glutMotionFunc(motion)
glutPassiveMotionFunc(None)
glutIdleFunc(desenhar)

glutIgnoreKeyRepeat(0)

glutMouseFunc(mouse)
glutKeyboardFunc(teclado_pressionar)
glutKeyboardUpFunc(teclado_soltar)

glutSpecialFunc(teclas_especiais_pressionar)
glutSpecialUpFunc(teclas_especiais_soltar)

print("Programa para teste das callbacks de mouse e teclado do glut.\n")
print("* Pressione as teclas '+' e '-' para aumentar e diminuir o raio da esfera.")
print("* Pressione as setas para mover o objeto na direcao pressionada.")
print("* Mova o objeto tambem com as teclas 'w', 's', 'a', 'd'.")
print("* Com o mouse, clique na tela para alterar a posicao do objeto.")
print("* Clique e arraste para mover o objeto.\n")
print("* Pressione 'm' para que o objeto mova sem o clique do mouse (passive motion).")
print("* Pressione ESC para sair!\n")
print("-------------------------------------------------------------------------")

glutMainLoop()

