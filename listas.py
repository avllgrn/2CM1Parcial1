from os import system
from random import randrange
import Pilas
import Colas

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos? '))

    conjunto1 = set()
    conjunto2 = set()
    P = Pilas.Pila()
    C = Colas.Cola()
        
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        print(f'Se agregan {x} y {y}')
        conjunto1.add(x)
        conjunto2.add(y)

    print(f'conjunto1 = {conjunto1}')
    print(f'conjunto2 = {conjunto2}')

    for i in conjunto1:
        P.push(i)

    for i in conjunto2:
        C.push(i)
        
    print('Pila')
    P.liberaMemoria()
    print()
    
    print('Cola')
    C.liberaMemoria()
    print()
