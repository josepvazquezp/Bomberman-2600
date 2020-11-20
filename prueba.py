import pygame
import time
import random

SCREENSIZE = 500
running = True
anchoDePixel = 10
altoDePixel = 10
direccion = ""
stop = False
vel = 10
x1 = 20
y1 = 10
x2 = 20
y2 = 60
x3 = 20
y3 = 70
x4 = 480
y4 = 10
mx = 480
my = 470
colC = False
v1 = True
t1 = True
move = True
lp1 = True
v2 = False
t2 = False
move2 = False
lp2 = False
v3 = False
t3 = False
move3 = False
lp3 = False
v4 = False
t4 = False
move4 = False
lp4 = False
vmonst = False
tm = False
moveM = False
cpb = False
game_over = False
inicio = True
mp = False
cFondo = (255, 231, 211)
gris = (128, 128, 128)
azul = (52, 79, 235)
rojo = (255, 0, 0)
morado = (168, 52, 235)
verde = (0, 255, 0)
negro = (0, 0, 0)
naranja = (255, 116, 0)
cyan = (0, 255, 255)
blanco = (255, 255, 255)
nar = (255, 119, 3)
aran = (255, 89, 0)
asus = (0, 189, 255)
moradin = (217, 52, 235)
vergde = (19, 191, 19)
mc = (176, 106, 44)

p1 = [(x1, y1)]

p2 = [(x2, y2)]

p3 = [(x3, y3)]

p4 = [(x4, y4)]

monstro = [(mx, my)]

contador = []

bomba = []

def mapaD(win):

    win.fill(cFondo)

    for x in range(50):
        for y in range(50):
            yC = y * 10
            if x % 2 != 0 and y % 2 == 0:
                xC = x * 10
                pygame.draw.rect(win, (gris), (xC, yC, anchoDePixel, altoDePixel))

    pygame.display.update()

def moverP(direccion, p):
    global stop

    nuevopX = p[0][0]
    nuevopY = p[0][1]

    p.pop()

    if direccion == "ARRIBA" and stop == True:
        nuevopY -= vel
        stop = False
    elif direccion == "ABAJO" and stop == True:
        nuevopY += vel
        stop = False
    elif direccion == "DERECHA" and stop == True:
        nuevopX += vel
        stop = False
    elif direccion == "IZQUIERDA" and stop == True:
        nuevopX -= vel
        stop = False

    p.insert(0, (nuevopX, nuevopY))

def dibujarP1(win, p1):

    for pixel in p1:
        pygame.draw.rect(win, (azul), (pixel[0], pixel[1], anchoDePixel, altoDePixel))

    pygame.display.update()

def colisionBordes(direccion, p):
    global colC
    global mp

    (x, y) = p[0]

    if x < 0 or x >= 500:
        if direccion == "DERECHA":
            p[0] = (x - vel, y)
            colC = True
        elif direccion == "IZQUIERDA":
            p[0] = (x + vel, y)
            colC = True
    elif y < 0 or y >= 500:
        if direccion == "ARRIBA":
            p[0] = (x, y + vel)
            colC = True
        elif direccion == "ABAJO":
            p[0] = (x, y - vel)
            colC = True

def colisonCuadros(direccion, p):
    global colC

    (xP, yP) = p[0]

    for x in range(50):
        for y in range(50):
            yC = y * 10
            if x % 2 != 0 and y % 2 == 0:
                xC = x * 10
                if xP == xC and yP == yC:
                    if direccion == "DERECHA":
                        p[0] = (xP - vel, yP)
                        colC = True
                    elif direccion == "IZQUIERDA":
                        p[0] = (xP + vel, yP)
                        colC = True
                    elif direccion == "ARRIBA":
                        p[0] = (xP, yP + vel)
                        colC = True
                    elif direccion == "ABAJO":
                        p[0] = (xP, yP - vel)
                        colC = True

def movI(contador):
    global move, move2, move3, move4
    global colC

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        contador.append(1)
    elif keys[pygame.K_LEFT]:
        contador.append(2)
    elif keys[pygame.K_UP]:
        contador.append(3)
    elif keys[pygame.K_DOWN]:
        contador.append(4)

    if colC == True and len(contador) != 0:
        contador.pop()
        colC = False

    if len(contador) == 4 and t1 == True:
        move = False
    elif len(contador) == 5 and t2 == True:
        move2 = False
    elif len(contador) == 5 and t3 == True:
        move3 = False
    elif len(contador) == 5 and t4 == True:
        move4 = False

def dibujarBomba(win, bomba, p1, p2, p3, p4):
    global move, move2, move3, move4

    keys = pygame.key.get_pressed()

    if move == False and t1 == True and keys[pygame.K_SPACE] and lp1 == False:
        (x1, y1) = p1[0]
        bomba.append((x1, y1))
        move = True

    elif move2 == False and t2 == True and keys[pygame.K_SPACE] and lp2 == False:
        (x2, y2) = p2[0]
        bomba.append((x2, y2))
        move2 = True

    elif move3 == False and t3 == True and keys[pygame.K_SPACE] and lp3 == False:
        (x3, y3) = p3[0]
        bomba.append((x3, y3))
        move3 = True

    elif move4 == False and t4 == True and keys[pygame.K_SPACE] and lp4 == False:
        (x4, y4) = p4[0]
        bomba.append((x4, y4))
        move4 = True

    pygame.display.flip()

    for pixel in bomba:
        pygame.draw.rect(win, (negro), (pixel[0], pixel[1], anchoDePixel, altoDePixel))

    pygame.display.update()

def movF(contador):
    global move, move2, move3, move4

    if move == True and t1 == True:
        if len(contador) >= 5:
            contador.clear()
        elif len(contador) == 4:
            move = False
    elif move2 == True and t2 == True:
        if len(contador) >= 6:
            contador.clear()
        elif len(contador) == 5:
            move2 = False
    elif move3 == True and t3 == True:
        if len(contador) >= 6:
            contador.clear()
        elif len(contador) == 5:
            move3 = False
    elif move4 == True and t4 == True:
        if len(contador) >= 6:
            contador.clear()
        elif len(contador) == 5:
            move4 = False

def finalTurno(bomba, contador):
    global t1, t2, t3, t4, tm
    global move, move2, move3, move4, moveM
    global lp1, lp2, lp3, lp4

    if len(bomba) >= 1:
        if v1 == True and t1 == True and move == False and len(bomba) == 1:
            t1 = False
            contador.clear()
            if v2 == True:
                t2 = True
                move2 = True
                lp2 = True
            elif v3 == True:
                t3 = True
                lp3 = True
                move3 = True
            elif v4 == True:
                t4 = True
                lp4 = True
                move4 = True
            elif vmonst == True:
                tm = True
                moveM = True
                contador.clear()
        elif vmonst == True and tm == True and moveM == False and len(bomba) == 2:
            tm = False
            contador.clear()
            if v1 == True:
                t1 = True
                lp1 = True
                move = True
        elif v2 == True and t2 == True and move2 == False and len(bomba) == 2:
            t2 = False
            contador.clear()
            if v3 == True:
                t3 = True
                lp3 = True
                move3 = True
            elif v4 == True:
                t4 = True
                lp4 = True
                move4 = True
            elif v1 == True:
                t1 = True
                lp1 = True
                move = True
        elif v3 == True and t3 == True and move3 == False and len(bomba) == 3:
            t3 = False
            contador.clear()
            if v4 == True:
                t4 = True
                lp4 = True
                move4 = True
            elif v1 == True:
                t1 = True
                lp1 = True
                move = True
        elif v4 == True and t4 == True and move4 == False and len(bomba) == 4:
            t4 = False
            contador.clear()
            if v1 == True:
                t1 = True
                lp1 = True
                move = True
        elif v1 == False and v2 == True and t2 == True and move2 == False and len(bomba) == 1:
            t2 = False
            contador.clear()
            if v3 == True:
                t3 = True
                lp3 = True
                move3 = True
            elif v4 == True:
                t4 = True
                lp4 = True
                move4 = True
        elif v1 == False and t3 == True and move3 == False and len(bomba) == 2:
            t3 = False
            contador.clear()
            if v4 == True:
                t4 = True
                lp4 = True
                move4 = True
            elif v2 == True:
                t2 = True
                move2 = True
                lp2 = True
        elif v2 == False and t3 == True and move3 == False and len(bomba) == 2:
            t3 = False
            contador.clear()
            if v4 == True:
                t4 = True
                lp4 = True
                move4 = True
            elif v1 == True:
                t1 = True
                lp1 = True
                move = True
        elif v1 == False and v2 == False and t3 == True and move3 == False and len(bomba) == 1:
            t3 = False
            contador.clear()
            if v4 == True:
                t4 = True
                lp4 = True
                move4 = True
        elif v1 == False and t4 == True and move4 == False and len(bomba) == 3:
            t4 = False
            contador.clear()
            if v2 == True:
                t2 = True
                move2 = True
                lp2 = True
        elif v1 == False and v2 == False and t4 == True and move4 == False and len(bomba) == 2:
            t4 = False
            contador.clear()
            if v3 == True:
                t3 = True
                lp3 = True
                move3 = True

def Bombayage(win, bomba):
    global move, move2, move3, move4, moveM
    global v1, v2, v3, v4, vmonst

    pygame.display.flip()

    explosion = []

    vivos = []

    if v1 == True:
        vivos.append(1)
    if v2 == True:
        vivos.append(1)
    if v3 == True:
        vivos.append(1)
    if v4 == True:
        vivos.append(1)
    if vmonst == True:
        vivos.append(1)

    if move2 == False and move3 == False and move4 == False and moveM == False and len(vivos) == len(bomba):
        (bX, bY) = bomba[0]
        dX = bX // 10
        dY = bY // 10
        (bX2, bY2) = bomba[1]
        dX2 = bX2 // 10
        dY2 = bY2 // 10
        if len(bomba) > 2:
            (bX3, bY3) = bomba[2]
            dX3 = bX3 // 10
            dY3 = bY3 // 10
            if len(bomba) == 4:
                (bX4, bY4) = bomba[3]
                dX4 = bX4 // 10
                dY4 = bY4 // 10
        for i in range(5):
            if dX % 2 == 0 and dY % 2 == 0:
                explosion.append((bX, bY + i * 10))
                explosion.append((bX, bY - i * 10))
            elif dX % 2 != 0 and dY % 2 != 0:
                explosion.append((bX + i * 10, bY))
                explosion.append((bX - i * 10, bY))
            else:
                explosion.append((bX, bY + i * 10))
                explosion.append((bX, bY - i * 10))
                explosion.append((bX + i * 10, bY))
                explosion.append((bX - i * 10, bY))
            if dX2 % 2 == 0 and dY2 % 2 == 0:
                explosion.append((bX2, bY2 + i * 10))
                explosion.append((bX2, bY2 - i * 10))
            elif dX2 % 2 != 0 and dY2 % 2 != 0:
                explosion.append((bX2 + i * 10, bY2))
                explosion.append((bX2 - i * 10, bY2))
            else:
                explosion.append((bX2, bY2 + i * 10))
                explosion.append((bX2, bY2 - i * 10))
                explosion.append((bX2 + i * 10, bY2))
                explosion.append((bX2 - i * 10, bY2))

            if len(bomba) > 2:
                if dX3 % 2 == 0 and dY3 % 2 == 0:
                    explosion.append((bX3, bY3 + i * 10))
                    explosion.append((bX3, bY3 - i * 10))
                elif dX3 % 2 != 0 and dY3 % 2 != 0:
                    explosion.append((bX3 + i * 10, bY3))
                    explosion.append((bX3 - i * 10, bY3))
                else:
                    explosion.append((bX3, bY3 + i * 10))
                    explosion.append((bX3, bY3 - i * 10))
                    explosion.append((bX3 + i * 10, bY3))
                    explosion.append((bX3 - i * 10, bY3))

                if len(bomba) == 4:
                    if dX4 % 2 == 0 and dY4 % 2 == 0:
                        explosion.append((bX3, bY3 + i * 10))
                        explosion.append((bX3, bY3 - i * 10))
                    elif dX4 % 2 != 0 and dY4 % 2 != 0:
                        explosion.append((bX3 + i * 10, bY3))
                        explosion.append((bX3 - i * 10, bY3))
                    else:
                        explosion.append((bX4, bY4 + i * 10))
                        explosion.append((bX4, bY4 - i * 10))
                        explosion.append((bX4 + i * 10, bY4))
                        explosion.append((bX4 - i * 10, bY4))

        if p1[0] in explosion:
            v1 = False
        if p2[0] in explosion:
            v2 = False
        if p3[0] in explosion:
            v3 = False
        if p4[0] in explosion:
            v4 = False
        if monstro[0] in explosion:
            vmonst = False

    for pixel in explosion:
        pygame.draw.rect(win, (naranja), (pixel[0], pixel[1], anchoDePixel, altoDePixel))

    vivos.clear()

    pygame.display.update()

def DibujarP2(win, p2):

    pygame.display.flip()

    for pixel in p2:
        pygame.draw.rect(win, (rojo), (pixel[0], pixel[1], anchoDePixel, altoDePixel))

    pygame.display.update()

def borrarE(bomba, contador):
    global t1, t2, t3, t4, tm
    global move, move2, move3, move4, moveM
    global lp1, lp2, lp3

    v = []

    if v1 == True:
        v.append(1)
    if v2 == True:
        v.append(1)
    if v3 == True:
        v.append(1)
    if v4 == True:
        v.append(1)
    if vmonst == True:
        v.append(1)

    if move2 == False and move3 == False and move4 == False and moveM == False and len(v) <= len(bomba):
        if v1 == True:
            t1 = True
            move = True
            lp1 = True
            bomba.clear()
            contador.clear()
        elif v1 == False and v2 == True:
            t2 = True
            move2 = True
            lp2 = True
            bomba.clear()
            contador.clear()
        elif v1 == False and v2 == False and v3 == True:
            t3 = True
            move3 = True
            lp3 = True
            bomba.clear()
            contador.clear()
        elif v4 == False:
            t1 = True
            move = True
            lp1 = True
            bomba.clear()
            contador.clear()

    v.clear()

def colPB(p1, p2, p3, p4, monstro, bomba, direccion):
    global colC
    global cpb
    global mp

    if v1 == True:
        if v2 == True and p1[0] == p2[0]:
            cpb = True
        elif v3 == True and p1[0] == p3[0]:
            cpb = True
        elif v4 == True and p1[0] == p4[0]:
            cpb = True
        elif vmonst == True and p1[0] == monstro[0]:
            cpb = True
    if v2 == True:
        if v3 == True and p2[0] == p3[0]:
            cpb = True
        elif v4 == True and p2[0] == p4[0]:
            cpb = True
    if v3 == True:
        if p3[0] == p4[0]:
            cpb = True
    if len(bomba) == 1:
        if v1 == True and v2 == True and p2[0] == bomba[0]:
            cpb = True
        elif v2 == True and v3 == True and p3[0] == bomba[0]:
            cpb = True
        elif v3 == True and v4 == True and p4[0] == bomba[0]:
            cpb = True
        elif v1 == True and vmonst == True and monstro[0] == bomba[0]:
            cpb = True
    elif len(bomba) == 2:
        if v3 == True:
            if p3[0] == bomba[0] or p3[0] == bomba[1]:
                cpb = True
        elif v4 == True:
            if p4[0] == bomba[0] or p4[0] == bomba[1]:
                cpb = True
    elif v4 == True and len(bomba) == 3:
        if p4[0] == bomba[0] or p4[0] == bomba[1] or p4[0] == bomba[2]:
            cpb = True

    if cpb == True:
        (x1, y1) = p1[0]
        (x2, y2) = p2[0]
        (x3, y3) = p3[0]
        (x4, y4) = p4[0]
        (xM, yM) = monstro[0]
        if direccion == "DERECHA":
            if t1 == True:
                p1[0] = (x1 - vel, y1)
            if t2 == True:
                p2[0] = (x2 - vel, y2)
            if t3 == True:
                p3[0] = (x3 - vel, y3)
            if t4 == True:
                p4[0] = (x4 - vel, y4)
            if tm == True and move == False:
                monstro[0] = (xM - vel, yM)
                mp = True
            colC = True
            cpb = False
        elif direccion == "IZQUIERDA":
            if t1 == True:
                p1[0] = (x1 + vel, y1)
            if t2 == True:
                p2[0] = (x2 + vel, y2)
            if t3 == True:
                p3[0] = (x3 + vel, y3)
            if t4 == True:
                p4[0] = (x4 + vel, y4)
            if tm == True and move == False:
                monstro[0] = (xM + vel, yM)
                mp = True
            colC = True
            cpb = False
        elif direccion == "ARRIBA":
            if t1 == True:
                p1[0] = (x1, y1 + vel)
            if t2 == True:
                p2[0] = (x2, y2 + vel)
            if t3 == True:
                p3[0] = (x3, y3 + vel)
            if t4 == True:
                p4[0] = (x4, y4 + vel)
            if tm == True and move == False:
                monstro[0] = (xM, yM + vel)
                mp = True
            colC = True
            cpb = False
        elif direccion == "ABAJO":
            if t1 == True:
                p1[0] = (x1, y1 - vel)
            if t2 == True:
                p2[0] = (x2, y2 - vel)
            if t3 == True:
                p3[0] = (x3, y3 - vel)
            if t4 == True:
                p4[0] = (x4, y4 - vel)
            if tm == True and move == False:
                monstro[0] = (xM, yM - vel)
                mp = True
            colC = True
            cpb = False

def gameOver():
    global game_over

    if v2 == False and v3 == False and v4 == False and vmonst == False:
        game_over = True
    elif v1 == False and v3 == False and v4 == False and vmonst == False:
        game_over = True
    elif v1 == False and v2 == False and v4 == False and vmonst == False:
        game_over = True
    elif v1 == False and v2 == False and v3 == False and vmonst == False:
        game_over = True
    elif v1 == False and vmonst == True:
        game_over = True

def dibujarGO(win):

    pygame.display.flip()

    if game_over == True:
        win.fill(negro)
        win.get_rect()
        font = pygame.font.Font(None, 80)
        fuente = pygame.font.Font(None, 30)
        text1 = font.render("Game Over", True, nar)
        text2 = fuente.render("Q", True, cyan)
        text3 = fuente.render("Quit", True, blanco)
        text1.get_rect()
        text2.get_rect()
        text3.get_rect()
        win.blit(text1, (100, 120))
        win.blit(text2, (160, 280))
        win.blit(text3, (190, 280))

        if v1 == True:
            f = pygame.font.Font(None, 60)
            text4 = f.render("P1 win", True, azul)
            text4.get_rect()
            win.blit(text4, (180, 200))
        elif v2 == True:
            f = pygame.font.Font(None, 60)
            text4 = f.render("P2 win", True, rojo)
            text4.get_rect()
            win.blit(text4, (180, 200))
        elif v3 == True:
            f = pygame.font.Font(None, 60)
            text4 = f.render("P3 win", True, morado)
            text4.get_rect()
            win.blit(text4, (180, 200))
        elif v4 == True:
            f = pygame.font.Font(None, 60)
            text4 = f.render("P4 win", True, verde)
            text4.get_rect()
            win.blit(text4, (180, 200))
        elif vmonst == True:
            f = pygame.font.Font(None, 60)
            text4 = f.render("Monster win", True, mc)
            text4.get_rect()
            win.blit(text4, (120, 200))
        else:
            f = pygame.font.Font(None, 60)
            text4 = f.render("Tie", True, blanco)
            text4.get_rect()
            win.blit(text4, (220, 200))

    pygame.display.update()

def salir(keys):
    global running

    if game_over == True:
        if keys[pygame.K_q]:
            running = False
    pygame.display.update()

def pantallaP2(win, keys, contador):
    global move2, lp2
    global direccion

    pygame.display.flip()

    if v2 == True and t2 == True and lp2 == True:
        move2 = False
        pygame.draw.rect(win, negro, (100, 150, 300, 150))
        f = pygame.font.Font(None, 60)
        fuente = pygame.font.Font(None, 30)
        text = f.render("Ready P2", True, rojo)
        text2 = fuente.render("Press", True, blanco)
        text3 = fuente.render("C", True, aran)
        text.get_rect()
        text2.get_rect()
        text3.get_rect()
        win.blit(text, (150, 200))
        win.blit(text2, (200, 250))
        win.blit(text3, (270, 250))

        if keys[pygame.K_c]:
            lp2 = False
            direccion = ""
            contador.clear()
            move2 = True
            time.sleep(0.0001)

    pygame.display.update()

def pantallaP1(win, keys, contador):
    global move, lp1
    global direccion

    if v1 == True and t1 == True and lp1 == True:
        move = False
        pygame.draw.rect(win, negro, (100, 150, 300, 150))
        f = pygame.font.Font(None, 60)
        fuente = pygame.font.Font(None, 30)
        text = f.render("Ready P1", True, azul)
        text2 = fuente.render("Press", True, blanco)
        text3 = fuente.render("C", True, cyan)
        text.get_rect()
        text2.get_rect()
        text3.get_rect()
        win.blit(text, (150, 200))
        win.blit(text2, (200, 250))
        win.blit(text3, (270, 250))

        if keys[pygame.K_c]:
            lp1 = False
            direccion = ""
            contador.clear()
            move = True

    pygame.display.flip()

def pantallaStart(win, keys):
    global inicio
    global v1, v2, v3, v4, vmonst

    if inicio == True:
        win.get_rect()
        f = pygame.font.Font(None, 90)
        p = pygame.font.Font(None, 32)
        b = pygame.font.Font(None, 30)
        bomber = f.render("Bomberman", True, cFondo)
        b2600 = f.render("2600", True, cFondo)
        n = p.render("Number of players: ", True, blanco)
        b1 = b.render("1", True, blanco)
        pres1 = b.render("Press 1", True, azul)
        b2 = b.render("2", True, blanco)
        pres2 = b.render("Press 2", True, rojo)
        b3 = b.render("3", True, blanco)
        pres3 = b.render("Press 3", True, morado)
        b4 = b.render("4", True, blanco)
        pres4 = b.render("Press 4", True, verde)
        by = b.render("By: JPVP and JMMM", True, asus)
        win.blit(bomber, (70, 60))
        win.blit(b2600, (180, 130))
        win.blit(n, (150, 240))
        win.blit(b1, (190, 280))
        win.blit(pres1, (210, 280))
        win.blit(b2, (190, 310))
        win.blit(pres2, (210, 310))
        win.blit(b3, (190, 340))
        win.blit(pres3, (210, 340))
        win.blit(b4, (190, 370))
        win.blit(pres4, (210, 370))
        win.blit(by, (150, 440))

        if keys[pygame.K_1]:
            vmonst = True
            inicio = False
        elif keys[pygame.K_2]:
            v2 = True
            inicio = False
        elif keys[pygame.K_3]:
            v2 = True
            v3 = True
            inicio = False
        elif keys[pygame.K_4]:
            v2 = True
            v3 = True
            v4 = True
            inicio = False

    pygame.display.update()

def pantallaP3(win, keys, contador):
    global move3, lp3
    global direccion

    if v3 == True and t3 == True and lp3 == True:
        move3 = False
        pygame.draw.rect(win, negro, (100, 150, 300, 150))
        f = pygame.font.Font(None, 60)
        fuente = pygame.font.Font(None, 30)
        text = f.render("Ready P3", True, morado)
        text2 = fuente.render("Press", True, blanco)
        text3 = fuente.render("C", True, moradin)
        text.get_rect()
        text2.get_rect()
        text3.get_rect()
        win.blit(text, (150, 200))
        win.blit(text2, (200, 250))
        win.blit(text3, (270, 250))

        if keys[pygame.K_c]:
            lp3 = False
            direccion = ""
            contador.clear()
            move3 = True

    pygame.display.flip()

def DibujarP3(win, p3):

    pygame.display.flip()

    for pixel in p3:
        pygame.draw.rect(win, (morado), (pixel[0], pixel[1], anchoDePixel, altoDePixel))

    pygame.display.update()

def pantallaP4(win, keys, contador):
    global move4, lp4
    global direccion

    if v4 == True and t4 == True and lp4 == True:
        move4 = False
        pygame.draw.rect(win, negro, (100, 150, 300, 150))
        f = pygame.font.Font(None, 60)
        fuente = pygame.font.Font(None, 30)
        text = f.render("Ready P4", True, verde)
        text2 = fuente.render("Press", True, blanco)
        text3 = fuente.render("C", True, vergde)
        text.get_rect()
        text2.get_rect()
        text3.get_rect()
        win.blit(text, (150, 200))
        win.blit(text2, (200, 250))
        win.blit(text3, (270, 250))

        if keys[pygame.K_c]:
            lp4 = False
            direccion = ""
            contador.clear()
            move4 = True

    pygame.display.flip()

def DibujarP4(win, p4):

    pygame.display.flip()

    for pixel in p4:
        pygame.draw.rect(win, (verde), (pixel[0], pixel[1], anchoDePixel, altoDePixel))

    pygame.display.update()

def dibujarMonstro(win, monstro):

    pygame.display.flip()

    for pixel in monstro:
        pygame.draw.rect(win, (mc), (pixel[0], pixel[1], anchoDePixel, altoDePixel))

    pygame.display.update()

def movIMonstro(monstro, p1, contador, bomba):
    global moveM
    global direccion
    global mp

    (mX, mY) = monstro[0]
    (pX, pY) = p1[0]

    xM = mX // 10
    yM = mY // 10


    direccion = ""

    keys = pygame.key.get_pressed()

    if len(contador) > 1:
        if keys[pygame.K_RIGHT]:
            contador.pop()
        elif keys[pygame.K_LEFT]:
            contador.pop()
        elif keys[pygame.K_UP]:
            contador.pop()
        elif keys[pygame.K_DOWN]:
            contador.pop()

    if len(contador) < 10:
        monstro.pop()
        r = random.randint(1, 2)
        if mp == True:
            if mX - pX > 0 and mY - pY > 0:
                pX *= 500
                pY *= 500
            elif mX - pX < 0 and mY - pY > 0:
                pX //= 500
                pY *= 500
            elif mX - pX > 0 and mY - pY < 0:
                pX *= 500
                pY //= 500
            elif mX - pX < 0 and mY - pY < 0:
                pX //= 500
                pY //= 500
            elif mX == pX and mY - pY < 0:
                pY //= 500
            elif mX == pX and mY - pY > 0:
                pY *= 500
            elif mY == pY and mX - pX > 0:
                pX *= 500
            elif mY == pY and mX - pX < 0:
                pX //= 500
        if xM % 2 == 0 and yM % 2 == 0:
            if mX - pX > 0 and mY - pY > 0:
                nuevoMx = mX
                nuevoMy = mY - vel
                contador.append(1)
                direccion = "ARRIBA"
            elif mX - pX < 0 and mY - pY > 0:
                nuevoMx = mX
                nuevoMy = mY - vel
                contador.append(1)
                direccion = "ARRIBA"
            elif mX - pX > 0 and mY - pY < 0:
                nuevoMx = mX
                nuevoMy = mY + vel
                contador.append(1)
                direccion = "ABAJO"
            elif mX - pX < 0 and mY - pY < 0:
                nuevoMx = mX
                nuevoMy = mY + vel
                contador.append(1)
                direccion = "ABAJO"
            elif mX == pX and mY - pY < 0:
                nuevoMx = mX
                nuevoMy = mY + vel
                contador.append(1)
                direccion = "ABAJO"
            elif mX == pX and mY - pY > 0:
                nuevoMx = mX
                nuevoMy = mY - vel
                contador.append(1)
                direccion = "ARRIBA"
            elif mY == pY:
                if r == 1:
                    nuevoMx = mX
                    nuevoMy = mY - vel
                    contador.append(1)
                    direccion = "ARRIBA"
                elif r == 2:
                    nuevoMx = mX
                    nuevoMy = mY + vel
                    contador.append(1)
                    direccion = "ABAJO"
        elif xM % 2 != 0 and yM % 2 != 0:
            if mX - pX > 0 and mY - pY > 0:
                nuevoMx = mX - vel
                nuevoMy = mY
                contador.append(1)
                direccion = "IZQUIERDA"
            elif mX - pX > 0 and mY - pY < 0:  # izq- abajo   2
                nuevoMx = mX - vel
                nuevoMy = mY
                contador.append(1)
                direccion = "IZQUIERDA"
            elif mX - pX < 0 and mY - pY > 0:  # der-arriba   2
                nuevoMx = mX + vel
                nuevoMy = mY
                contador.append(1)
                direccion = "DERECHA"
            elif mX - pX < 0 and mY - pY < 0:  # dercha- abajo 2
                nuevoMx = mX + vel
                nuevoMy = mY
                contador.append(1)
                direccion = "DERECHA"
            elif mX == pX:
                if r == 1:
                    nuevoMx = mX - vel
                    nuevoMy = mY
                    contador.append(1)
                    direccion = "IZQUIERDA"
                elif r == 2:
                    nuevoMx = mX + vel
                    nuevoMy = mY
                    contador.append(1)
                    direccion = "DERECHA"
            elif mY == pY and mX - pX > 0:
                nuevoMx = mX - vel
                nuevoMy = mY
                contador.append(1)
                direccion = "IZQUIERDA"
            elif mY == pY and mX - pX < 0:
                nuevoMx = mX + vel
                nuevoMy = mY
                contador.append(1)
                direccion = "DERECHA"
        else:
            if mX - pX > 0 and mY - pY > 0:
                if r == 1:
                    nuevoMx = mX - vel
                    nuevoMy = mY
                    contador.append(1)
                    direccion = "IZQUIERDA"
                elif r == 2:
                    nuevoMx = mX
                    nuevoMy = mY - vel
                    contador.append(1)
                    direccion = "ARRIBA"
            elif mX - pX > 0 and mY - pY < 0:  # izq- abajo   2
                if r == 1:
                    nuevoMx = mX - vel
                    nuevoMy = mY
                    contador.append(1)
                    direccion = "IZQUIERDA"
                elif r == 2:
                    nuevoMx = mX
                    nuevoMy = mY + vel
                    contador.append(1)
                    direccion = "ABAJO"
            elif mX - pX < 0 and mY - pY > 0:  # der-arriba   2
                if r == 1:
                    nuevoMx = mX + vel
                    nuevoMy = mY
                    contador.append(1)
                    direccion = "DERECHA"
                elif r == 2:
                    nuevoMx = mX
                    nuevoMy = mY - vel
                    contador.append(1)
                    direccion = "ARRIBA"
            elif mX - pX < 0 and mY - pY < 0:  # dercha- abajo 2
                if r == 1:
                    nuevoMx = mX + vel
                    nuevoMy = mY
                    contador.append(1)
                    direccion = "DERECHA"
                elif r == 2:
                    nuevoMx = mX
                    nuevoMy = mY + vel
                    contador.append(1)
                    direccion = "ABAJO"
            elif mX == pX and mY - pY < 0:
                nuevoMx = mX
                nuevoMy = mY + vel
                contador.append(1)
                direccion = "ABAJO"
            elif mX == pX and mY - pY > 0:
                nuevoMx = mX
                nuevoMy = mY - vel
                contador.append(1)
                direccion = "ARRIBA"
            elif mY == pY and mX - pX > 0:
                nuevoMx = mX - vel
                nuevoMy = mY
                contador.append(1)
                direccion = "IZQUIERDA"
            elif mY == pY and mX - pX < 0:
                nuevoMx = mX + vel
                nuevoMy = mY
                contador.append(1)
                direccion = "DERECHA"

        monstro.insert(0, (nuevoMx, nuevoMy))

    if len(contador) == 6:
        bomba.append((mX, mY))

    elif len(contador) == 10:
        moveM = False
        mp = False

def main():
    global running
    global direccion
    global stop

    pygame.init()
    win = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))
    pygame.display.set_caption("Bomberman 2600")

    while running:
        clock = pygame.time.Clock()
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            direccion = "DERECHA"
            stop = True
        elif keys[pygame.K_LEFT]:
            direccion = "IZQUIERDA"
            stop = True
        elif keys[pygame.K_UP]:
            direccion = "ARRIBA"
            stop = True
        elif keys[pygame.K_DOWN]:
            direccion = "ABAJO"
            stop = True

        pantallaStart(win, keys)

        if game_over == False and inicio == False:
            mapaD(win)

            if v1 == True:
                pantallaP1(win, keys, contador)

                dibujarP1(win, p1)
                if t1 == True and move == True:
                    moverP(direccion, p1)

                    colisionBordes(direccion, p1)

                    colisonCuadros(direccion, p1)

            colPB(p1, p2, p3, p4, monstro, bomba, direccion)

            movI(contador)

            if t1 == True or t2 == True or t3 == True or t4 == True or tm == True:
                dibujarBomba(win, bomba, p1, p2, p3, p4)

            movF(contador)

            finalTurno(bomba, contador)

            if v2 == True:
                pantallaP2(win, keys, contador)

                DibujarP2(win, p2)
                if t2 == True and move2 == True:
                    moverP(direccion, p2)

                    colisionBordes(direccion, p2)

                    colisonCuadros(direccion, p2)

            if v3 == True:
                pantallaP3(win, keys, contador)

                DibujarP3(win, p3)
                if t3 == True and move3 == True:
                    moverP(direccion, p3)

                    colisionBordes(direccion, p3)

                    colisonCuadros(direccion, p3)

            if v4 == True:
                pantallaP4(win, keys, contador)

                DibujarP4(win, p4)
                if t4 == True and move4 == True:
                    moverP(direccion, p4)

                    colisionBordes(direccion, p4)

                    colisonCuadros(direccion, p4)

            if vmonst == True:
                dibujarMonstro(win, monstro)

                if tm == True and moveM == True:
                    movIMonstro(monstro, p1, contador, bomba)

                    colisionBordes(direccion, monstro)

                    colisonCuadros(direccion, monstro)

            Bombayage(win, bomba)

            time.sleep(0.0001)

            borrarE(bomba, contador)

        if inicio == False:
            gameOver()

            dibujarGO(win)

            salir(keys)

main()