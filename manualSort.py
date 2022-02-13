def manualSort(n) :
    temp = 0
    n.sort()
    for i in n:
        if i == n[0]:
            temp = i
        elif i == (temp + 1):
            temp = i
        else :
            result = i-1
            break
    return result

if __name__ == "__main__" :
    n = list(map(int, input('enter: ')))
    print(manualSort(n))
