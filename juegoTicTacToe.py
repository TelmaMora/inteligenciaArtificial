# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fXpHU2XmER54VD0vL3PIo25aX_MqVR11
"""

import random

def dibujarTablero(tablero):
    print('   |   |')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('   |   |')

def elegirLetra():
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('Elige tu letra (X o O)?')
        letra = input().upper()
    return letra
    

def primero():
    if random.randint(0, 1) == 0:
        return 'computadora'
    else:
        return 'jugador'

def hacerMovimiento(tablero, letra, movimiento):
    tablero[movimiento] = letra

def verificar(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def duplicar(tablero):
    copia = []

    for i in tablero:
        copia.append(i)

    return copia

def disponible(tablero, movimiento):
    return tablero[movimiento] == ' '

def movimientoJugador(tablero):
    movimiento = ' '
    while movimiento not in '1 2 3 4 5 6 7 8 9'.split() or not disponible(tablero, int(movimiento)):
        print('Elige una posicion (1-9)')
        movimiento = input()
    return int(movimiento)

def escogerMovimiento(tablero, listaM):
    posibles = []
    for i in listaM:
        if disponible(tablero, i):
            posibles.append(i)

    if len(posibles) != 0:
        return random.choice(posibles)
    else:
        return None

def movmientoCompu(tablero, letraC):
    if letraC == 'X':
        letraJ = 'O'
    else:
        letraJ = 'X'

    for i in range(1, 10):
        copia = duplicar(tablero)
        if disponible(copia, i):
            hacerMovimiento(copia, letraC, i)
            if verificar(copia, letraC):
                return i

    for i in range(1, 10):
        copia = duplicar(tablero)
        if disponible(copia, i):
            hacerMovimiento(copia, letraJ, i)
            if verificar(copia, letraJ):
                return i

    movimiento = escogerMovimiento(tablero, [1, 3, 7, 9])
    if movimiento != None:
        return movimiento

    if disponible(tablero, 5):
        return 5

    return escogerMovimiento(tablero, [2, 4, 6, 8])

def estaLleno(tablero):
    for i in range(1, 10):
        if disponible(tablero, i):
            return False
    return True


while True:
    tab = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    letraJ=elegirLetra()
    if letraJ == 'X':
        letraC = 'O'
    else:
        letraC ='X'
    turno = primero()
    print(turno + ' empieza.')
    jugando = True

    while jugando:
        if turno == 'jugador':
            dibujarTablero(tab)
            movimiento = movimientoJugador(tab)
            hacerMovimiento(tab, letraJ, movimiento)

            if verificar(tab, letraJ):
                dibujarTablero(tab)
                print('----------------------------------------------------------')
                print('??GANASTE!')
                jugando = False
            else:
                if estaLleno(tab):
                    dibujarTablero(tab)
                    print('----------------------------------------------------------')
                    print('??ES UN EMPATE!')
                    break
                else:
                    turno = 'computadora'

        else:
            movimiento = movmientoCompu(tab, letraC)
            hacerMovimiento(tab, letraC, movimiento)

            if verificar(tab, letraC):
                dibujarTablero(tab)
                print('----------------------------------------------------------')
                print('??PERDISTE!')
                jugando = False
            else:
                if estaLleno(tab):
                    dibujarTablero(tab)
                    print('----------------------------------------------------------')
                    print('??ES UN EMPATE!')
                    break
                else:
                    turno = 'jugador'
    break