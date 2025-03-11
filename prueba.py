import os
os.system('cls')

cadena = input('Dame cadena ')

for caracter in cadena:
    if caracter.isalnum():
        print(caracter.upper())