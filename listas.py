from os import system
from math import pow, sqrt

def raicesFormulaGeneral(a, b, c):
    x1 = None
    x2 = None
    
    disc = pow(b,2)-4*a*c
    if disc < 0:
        print('Error! Raíces imaginarias...')
    elif a == 0:
        print('Error! Raíces indeterminadas...')
    else:
        x1 = (-b+sqrt(disc))/(2*a)
        x2 = (-b-sqrt(disc))/(2*a)
    
    return x1,x2

if __name__ == '__main__':
    system('cls')

    x = raicesFormulaGeneral(1,1,1)
    print(f'x={x} type={type(x)}, len={len(x)}')
    x1 = x[0]
    x2 = x[1]
    print(f'x1={x1}\tx2={x2}\n')

    x = raicesFormulaGeneral(0,1,1)
    print(f'x={x} type={type(x)}, len={len(x)}')
    x1 = x[0]
    x2 = x[1]
    print(f'x1={x1}\tx2={x2}\n')

    x = raicesFormulaGeneral(-1,1,1)
    print(f'x={x} type={type(x)}, len={len(x)}')
    x1 = x[0]
    x2 = x[1]
    print(f'x1={x1}\tx2={x2}\n')

