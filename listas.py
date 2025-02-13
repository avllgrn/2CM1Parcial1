from os import system
from random import randrange

def unaFuncionConInput():
    V = []
    print(V, type(V), len(V))

    n = int(input('Cuantos? '))

    for i in range(n):
        dato = float(input(f'Ingresa el dato {i} '))
        V.append(dato)
        print(i, V[i], type(V[i]))
    print(V, type(V), len(V))

def unaFuncionConRandRange():
    V = []
    print(V, type(V), len(V))

    n = int(input('Cuantos? '))

    for i in range(n):
        V.append(randrange(101)/10)
        print(i, V[i], type(V[i]))
    print(V, type(V), len(V))

if __name__ == '__main__':
    system('cls')
    unaFuncionConInput()
    print()
    unaFuncionConRandRange()
    print()