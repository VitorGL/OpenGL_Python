from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
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
camera_y = 80
camera_z = 200
rot_camera = False
angulo = 0
fAspect = largura/altura

visao_x = 0
visao_y = 0
visao_z = 0

# Funções


# Inicializa opengl
def inicializar():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_SMOOTH)

    glEnable(GL_LIGHT0)  # habilita luz 0
    glEnable(GL_COLOR_MATERIAL)  # Utiliza cor do objeto como material
    glColorMaterial(GL_FRONT, GL_DIFFUSE)

    glEnable(GL_LIGHTING)  # Habilita luz
    glEnable(GL_DEPTH_TEST)  # Habilita Z - buffer
    glEnable(GL_CULL_FACE)  # Habilita Backface - Culling


def idle():
    glutPostRedisplay()


# Eixos coordenados
def desenha_eixos():
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-10.0, 0.0, 0.0)
    glVertex3f(10.0, 0.0, 0.0)
    glColor3f(0.0,   1.0, 0.0)
    glVertex3f(0.0, -10.0, 0.0)
    glVertex3f(0.0,  10.0, 0.0)
    glEnd()


def desenha_objetos():
    glColor3f(0.0, 0.0, 1.0)

    glutWireTeapot(35)
    glTranslatef(0, -28, 0)


#############################
# Glut and image functions
def exibir():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    definir_visualizacao()

    desenha_objetos()

    glColor3f(1, 0, 1)
    glLineWidth(3)
    glBegin(GL_LINES)
    for z in range(1000)[::10]:
        glVertex3f(-1000, -0.1, z)
        glVertex3f(1000, -0.1, z)

    for x in range(1000)[::10]:
        glVertex3f(x, -0.1, -1000)
        glVertex3f(x, -0.1, 1000)

    glEnd()
    glLineWidth(1)

    glutSwapBuffers()
    glutPostRedisplay()


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

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    # Especifica a projeção perspectiva(angulo, aspecto, zMin, zMax)
    gluPerspective(angulo, fAspect, 0.5, 500)

    # posicionaObservador()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(camera_x, camera_y, camera_z,
              visao_x, visao_y, visao_z, 0, 1, 0)


def teclado_pressionar(tecla, x, y):

    if tecla == b'\x1b':
        exit(0)
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


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(int(largura), int(altura))
glutInitWindowPosition(20, 20)
glutCreateWindow("Viewport Test")
inicializar()
glutDisplayFunc(exibir)
glutReshapeFunc(reformatar)
glutMouseFunc(mouse)
glutKeyboardFunc(teclado_pressionar)
glutSpecialFunc(teclas_especiais_press)
glutSpecialUpFunc(teclas_especiais_soltar)
glutIdleFunc(idle)
glutMainLoop()
