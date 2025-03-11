from os import system
import Pilas

def esExpresionCorrecta(expresion):
    P = Pilas.Pila()

    for simbolo in expresion:
        if simbolo == '(':
            P.push(')')
        elif simbolo == ')' and P.estaVacia():
            return False
        elif simbolo == ')' and not P.estaVacia():
            P.pop()

    if P.estaVacia():
        return True
    else:
        return False

if __name__ == '__main__':
    system('cls')
    
    expresion = input('Ingresa expresion ')
    
    if esExpresionCorrecta(expresion):
        print(f'{expresion} EStÁ correcta =)')
    else:
        system('cls')
        print(f'{expresion} NO ESTÁ correcta =(')