import sys

def isReal(num):
    try:
        float(num)
        return True
    except:
        return False

class BiquadEq:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _descriminant(self):
        return self.b**2 - 4*self.a*self.c

    def roots(self):
        D = self._descriminant()
        roots = []

        if (D < 0): 
            return ()
        elif (D == 0):
            root1 = ((-self.b) / (2*self.a))**0.5
            if isReal(root1): roots.append(root1)
            root2 = -((-self.b) / (2*self.a))**0.5
            if isReal(root2): roots.append(root2)
            return tuple(roots)
        else:
            root1 = ((-self.b + D**0.5) / (2 * self.a))**0.5
            if isReal(root1): roots.append(root1)
            root2 = ((-self.b - D**0.5) / (2 * self.a))**0.5
            if isReal(root2): roots.append(root2)
            root3 = -((-self.b + D**0.5) / (2 * self.a))**0.5
            if isReal(root3): roots.append(root3)
            root4 = -((-self.b - D**0.5) / (2 * self.a))**0.5
            if isReal(root4): roots.append(root4)
            return tuple(roots)

def main():
    a, b, c = 0, 0, 0
    if len(sys.argv) != 4 or float(sys.argv[1]) == 0:
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

    eq = BiquadEq(a, b, c)
    roots = eq.roots()
    if len(roots) == 0:
        print("Корней нет!")
    else:
        print(*roots)

if __name__ == "__main__":
    main()