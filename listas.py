from os import system

if __name__ == '__main__':
    system('cls')
    
    n = int(input('Dame n '))
    
    s = 0
    for i in range(n+1):
        s = s+i
        print(f'i = {i}\ts = {s}')

    print(f'\n\ns = {s}')
