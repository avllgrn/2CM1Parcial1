from os import system

class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente =siguiente

    def __str__(self):
        cadena = '| '
        cadena += str(self.dato) + ' |'
        if self.siguiente != None:
            cadena += ' -> '
        return cadena

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def __del__(self):
        self.liberaMemoria()

    def liberaMemoria(self):
        while not self.estaVacia():
            print(self.pop())

    def estaVacia(self):
        return self.primero==None and self.ultimo==None

    def push(self, dato):
        if self.estaVacia():
            self.primero = Nodo(dato, None)
            self.ultimo = self.primero

        else:
            self.ultimo.siguiente = Nodo(dato, None)
            self.ultimo = self.ultimo.siguiente

    def pop(self):
        dato = None
        if not self.estaVacia():
            dato = self.primero.dato
            if self.primero != self.ultimo:
                aux = self.primero
    
                self.primero = self.primero.siguiente
                del aux

            else:
                del self.primero
                self.primero = None
                self.ultimo = None

        return dato
    
if __name__ == '__main__':
    system('cls')
    
    P = Cola()

    P.push(5)
    P.push(3)
    P.push(7)
    P.push(-4)

    print(P.pop())
    print(P.pop())
    
    P.push(9)

    print(P.pop())
    print(P.pop())
    print(P.pop())
    print(P.pop())
