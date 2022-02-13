def Cacah(n) :
    result = []
    a = 1
    b = 1
    c = 0
    for i in range(n):
        c = c+1
        if c % 9 == 0:
            result.append('z')
            a = a+1
        elif c % 3 == 0:
            result.append(b*7)
            b = b+1
        else: 
            result.append(a*3)
            a = a+1
            
    return result
    
if __name__ == "__main__" :
    n = int(input("enter: "))
    print(Cacah(n))
