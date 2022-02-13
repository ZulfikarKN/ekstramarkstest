if __name__ == "__main__":
    n = int(input('angka: '))
    counter = n
    if (n % 2 == 0):
        print('Harus Bilangan Ganjil')
    else :
        for i in range(n):
            counter -= 1
            if (i == 0) or (i == (n-1)):
                for a in range(n-1):
                    print('x', end='')
            else :
                for b in range(n-1):
                    if (b == 0):
                        print('x', end='')
                    elif (b == counter):
                        print('x', end='')
                    else: print('o', end='')
            print('x')
