from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')
    
    V = []
    n = int(input('Dame n '))

    for i in range(n):
        V.append(randrange(-100, 101))

    for i in range(n):
        print(f'V[{i}] = {V[i]}')
    print('\n\n')
        
    s = 0
    i=0
    while i<n:
        s = s+V[i]
        #print(f'V[{i}] = {V[i]}\ts = {s}')
        i += 1

    print(f's = {s}')
    if n>0:
        promedio = s/n
        print(f'promedio = {promedio}')

    menor = V[0]
    posMenor = 0
    i=0
    while i<n:
        if V[i] < menor:
            menor = V[i]
            posMenor = i
        #print(f'menor = {menor} = V[{i}]')
        i += 1
    print(f'menor = {menor} = V[{posMenor}]')


    mayor = V[0]
    posMenor = 0
    i=0
    while i<n:
        if V[i] > mayor:
            mayor = V[i]
            posMenor = i
        #print(f'mayor = {mayor} = V[{i}]')
        i += 1
    print(f'mayor = {mayor} = V[{posMenor}]')

    menorQuePromedio = 0
    i=0
    while i<n:
        if V[i] < promedio:
            menorQuePromedio += 1
        i += 1
    print(f'Hay {menorQuePromedio} valores menores que el promedio')


    mayorQuePromedio = 0
    i=0
    while i<n:
        if V[i] > promedio:
            mayorQuePromedio += 1
        i += 1
    print(f'Hay {mayorQuePromedio} valores mayores que el promedio')
