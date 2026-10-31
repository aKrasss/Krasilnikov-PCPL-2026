import sys

def isReal(num):
    try:
        float(num)
        return True
    except:
        return False

def descriminant(a, b, c):
    return b**2 - 4*a*c

def roots4(a, b, c):
    D = descriminant(a, b, c)
    roots = []
    if (D < 0): 
        return ()
    elif (D == 0):
        root1 = (-b/(2*a))**0.5
        if isReal(root1): roots.append(root1)
        root2 = -(-b/(2*a))**0.5
        if isReal(root2): roots.append(root2)
        return tuple(roots)
    else:
        root1 = ((-b+D**0.5)/(2*a))**0.5
        if isReal(root1): roots.append(root1)
        root2 = ((-b-D**0.5)/(2*a))**0.5
        if isReal(root2): roots.append(root2)
        root3 = -((-b+D**0.5)/(2*a))**0.5
        if isReal(root3): roots.append(root3)
        root4 = -((-b-D**0.5)/(2*a))**0.5
        if isReal(root4): roots.append(root4)
        return tuple(roots)

def main():
    a, b, c = 0, 0, 0
    if (len(sys.argv) != 4 or float(sys.argv[1]) == 0):
        print("Количество аргументов, указанное в командной строке, недостаточно (должно быть 3)")
        while a == 0:
            print("Введите аргументы a, b, c; a не может быть равно 0!")
            try:
                a, b, c = map(float, input().split())
            except:
                continue
    else:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    roots = roots4(a, b, c)
    if len(roots) == 0:
        print("Корней нет!")
    else:
        print(*roots)

if __name__ == "__main__":
    main()
