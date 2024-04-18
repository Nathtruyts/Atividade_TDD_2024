class Triangle:
    def __init__(self):
        pass

    def check_triangle(self, a, b, c) -> str:
        if not self.triangle_is_valid(a, b, c):
            return "Não é um triângulo válido"
        elif self.is_equilateral(a, b, c):
            return "Triangulo Equilatero"
        elif self.is_isosceles(a, b, c):
            return "Triangulo Isosceles"
        else:
            return "Triangulo Escaleno"

    def triangle_is_valid(self, a: int, b: int, c: int) -> bool:
        if a <= 0 or b <= 0 or c <= 0:
            return False
        elif a + b <= c or a + c <= b or b + c <= a:
            return False
        else:
            return True

    def is_isosceles(self, a: int, b: int, c: int) -> bool:
        if a == b or a == c or b == c:
            return True
        else:
            return False

    def is_equilateral(self, a: int, b: int, c: int) -> bool:
        return a == b == c
