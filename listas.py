from os import system

if __name__ == '__main__':
    system('cls')
    
    n = int(input('Dame n '))
    
    p = 1
    for i in range(1, n+1):
        p = p*i
        print(f'i = {i}\tp = {p}')

    print(f'\n\np = {p}')
