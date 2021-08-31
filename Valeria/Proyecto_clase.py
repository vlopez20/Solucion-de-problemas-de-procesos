# Nombre: Valeria Natalí López de León
# Matricula: A01283512
# Memorama : razas de perros

"""
Este programa tiene como propósito mostrar la forma de utilizar
matrices en Python como listas de listas.
"""
import random

''' Función que crea y regresa una matriz de tamaño tam_ren X tam_col
    inicializada con 0s. Observa que los subíndices de la matriz son
    valores que van de 0  a tam-1.'''
def crea_matriz(tam_ren, tam_col):
    matriz=[] 
    for ren in range(tam_ren):
        matriz.append(['-'] * tam_col)
    return matriz


''' Despliega en pantalla la matriz que recibe como parámetro
de entrada: puede ser el tablero o juego '''
def desplegar(mat):
    """
    Función que muestra en la pantalla los datos de la matriz mat.
    """
    for ren in range(len(mat)):
        for col in range(len(mat[ren])):
            print(f'{mat[ren][col]:17}', end='')
        print()
        
    print('\n')
    
''' función que recibe el tablero y el tiro del jugador -
la función calcula el r y c correspondientes al tiro'''
def leer_tiro(tablero, t):
    tiro=int(input('Carta:'))
    r1=tiro//6
    c1=tiro%6
    
    while((tiro==t) or (tiro<0) or (tiro>35) or (tablero[tiro//6][tiro%6]!=tiro)):
        if t==-1:
            tiro=int(input('Error carta 1:'))
            r1=tiro//6
            c1=tiro%6
        else:
            tiro=int(input('Error carta 2:'))
            r1=tiro//6
            c1=tiro%6
    return tiro
'''
Recibe como parámetros la matriz tablero y la matriz juego
así como los 2 tiros del jugador -el cual es un valor entre
0..35
Despliega en pantalla el tablero que recibe como parámetro
de entrada: y muestra las cartas que eligio el jugador indicadas
en la matriz juego[r1][c1], juego[r2][c2]
si son iguales juego[r1][c1]== juego[r2][c2] entonces se reemplazan
en el tablero -
por eso ahora esta función retorna el tablero modificado o
sin modificar en caso que no sean iguales
'''
def desplegar_tablero_jugador(tablero,juego,tiro1,tiro2):
    r1=tiro1//6
    c1=tiro1%6
    r2=tiro2//6
    c2=tiro2%6
    

    for ren in range(len(tablero)):
        for col in range(len(tablero[ren])):
            if ren == r1 and col == c1 or ren == r2 and col == c2:
                print(f'{juego[ren][col]:17}', end = ' ')
            else:
                print(f'{tablero[ren][col]:17}', end = ' ')    
        print()
        
    if juego[r1][c1] == juego[r2][c2]:
        tablero[r1][c1]=juego[r1][c1]
        tablero[r2][c2]=juego[r2][c2]
                    
    return tablero
        

                               
   
'''Función que inicializa el tablero de 6X6 con
valores del 0 al 35, son las posiciones donde podrán
tirar los 2 jugadores'''    
def inicializar_tablero(matriz):
    valor=0
    for iR in range(len(matriz)):
        for iC in range(len(matriz[iR])):
            matriz[iR][iC]= valor
            valor = valor + 1
    return matriz

'''Función que inicializa el juego de 6X6 con
valores del 0 al 17 repetido 2 veces y revuelto'''
def inicializar_juego(matriz):
    lista=['labrador','pitbull','pug','husky','bulldog','pomerania','chihuahua','poodle',\
       'beagle','golden retriever','san bernardo','corgi','pastor alemán','spitz japonés',\
       'border collie','dóberman', 'cocker','dálmata']
    # se repitan 2 veces los mismo valores
    lista=lista*2
    random.shuffle(lista)
 
    carta=0
    for iR in range(len(matriz)):
        for iC in range(len(matriz[iR])):
            matriz[iR][iC]=lista[carta]
            carta=carta+1
           
    return matriz

    
def main():
    #llamada a las funciones 
    juego = crea_matriz(6,6)
    tablero = crea_matriz(6,6)
    tablero = inicializar_tablero(tablero)
    juego = inicializar_juego(juego)

    cj1=0
    cj2=0
    resp='si'
    #desplegar tablero inicial
    print('tablero') 
    desplegar(tablero)

    

    
    while(resp.lower()=='si' and (cj1+cj2<18)):
        print('turno jugador 1')
        tiro1=leer_tiro(tablero,-1)
        tiro2=leer_tiro(tablero, tiro1)
        tablero=desplegar_tablero_jugador(tablero,juego,tiro1,tiro2)
       
    
        #variables
        r1=tiro1//6
        c1=tiro1%6
        r2=tiro2//6
        c2=tiro2%6
        
       
        if juego[r1][c1]!= juego[r2][c2]:
            print('puntos jugador 0')
        else:
            cj1 +=1
            print('puntos jugador 1:', cj1)
   
           
           
        resp=input('¿Quieres seguir jugando? Si/No')
        if resp.lower()=='si':   
            desplegar(tablero)
            print('turno jugador 2')
            tiro1=leer_tiro(tablero,-1)
            tiro2=leer_tiro(tablero,tiro1)
            tablero=desplegar_tablero_jugador(tablero, juego, tiro1, tiro2)
          
            
            if juego[r1][c1]!= juego[r2][c2]:
                print('puntos jugador 0')
            else:
                cj2 +=1
                print('puntos jugador 1:', cj2)
   
            resp=input('¿Quieres seguir jugando? Si/No')
        

           
            
main()
