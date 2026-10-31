import sys

def isReal(num: float) -> bool:
    try: 
        float(num)
        return True
    except:
        return False

def roots(a: float, b: float, c: float) -> tuple:
    D = b**2 - 4*a*c
    roots = []
    match D:
        case _ if D < 0:
            return ()
        case _ if D == 0:
            root1 = (-b/(2*a))**0.5
            if isReal(root1): roots.append(root1)
            root2 = -(-b/(2*a))**0.5
            if isReal(root2): roots.append(root2)
            return tuple(roots)
        case _:
            root1 = ((-b+D**0.5)/(2*a))**0.5
            if isReal(root1): roots.append(root1)
            root2 = ((-b-D**0.5)/(2*a))**0.5
            if isReal(root2): roots.append(root2)
            root3 = -((-b+D**0.5)/(2*a))**0.5
            if isReal(root3): roots.append(root3)
            root4 = -((-b-D**0.5)/(2*a))**0.5
            if isReal(root4): roots.append(root4)
            return tuple(roots)

def printRoots(roots_: tuple) -> str:
    match roots_:
        case []: 
            return "Корней нет!"
        case (root1, root2):
            return f"2 {root1} {root2}"
        case (root1, root2, root3, root4):
            return f"{root1} {root2} {root3} {root4}"
        case _:
            return "Неизвестный результат!"

def main():
    a, b, c = 0, 0, 0
    match sys.argv[1:]:
        case [aStr, bStr, cStr]:
            if float(aStr) != 0:
                a, b, c = map(float, [aStr, bStr, cStr])
            else:
                print("Аргумент a не должен быть равен 0!")
        case _:
            print("Количество аргументов, указанное в командной строке, недостаточно (должно быть 3)")
    while a == 0:
        print("Введите аргументы a, b, c; a не может быть равно 0!")
        try:
            a, b, c = map(float, input().split())
        except:
            continue
    print(printRoots(roots(a, b, c)))

if __name__ == "__main__":
    main()