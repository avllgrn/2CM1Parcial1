from os import system

def unaFuncionConUnaListaDeEnteros():
    lista = [21, 2, -3, 42, 5]
    print(lista, type(lista), len(lista))

    for i in range(len(lista)):
        print(i, lista[i], type(lista[i]))

def unaFuncionConUnaListaDeFlotantes():
    lista = [21.1, 2.5, -3.25, -1.75]
    print(lista, type(lista), len(lista))

    for i in range(len(lista)):
        print(i, lista[i], type(lista[i]))

def unaFuncionConUnaListaDeStrings():
    lista = ['casa', 'ventana', 'puerta']
    print(lista, type(lista), len(lista))

    for i in range(len(lista)):
        print(i, lista[i], type(lista[i]))

if __name__ == '__main__':
    system('cls')
    unaFuncionConUnaListaDeEnteros()
    print()
    unaFuncionConUnaListaDeFlotantes()
    print()
    unaFuncionConUnaListaDeStrings()
    print()
