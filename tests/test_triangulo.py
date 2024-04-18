import sys, os

cur_path = os.path.dirname(os.path.abspath(__file__))
head, tail = os.path.split(os.path.split(cur_path)[0])
sys.path.insert(0, os.path.join(head, 'src'))
sys.path.insert(1, os.path.join(head, 'tests'))



import pytest
from src.main import Triangle

@pytest.fixture(scope="function")
def triangule():
    return Triangle()


def test_is_escaleno(triangule: Triangle):
    ret = triangule.check_triangle(10, 8, 4)
    assert ret == "Triangulo Escaleno"


def test_is_isosceles(triangule: Triangle):
    ret = triangule.check_triangle(10, 10, 8)
    assert ret == "Triangulo Isosceles"


def test_is_equilateral(triangule: Triangle):
    ret = triangule.check_triangle(10, 10, 10)
    print(ret)
    assert ret == "Triangulo Equilatero"


@pytest.mark.parametrize("a, b, c, tipo", [
    (5, 5, 3, "Triangulo Isosceles"),
    (7, 7, 2, "Triangulo Isosceles"),
    (4, 4, 6, "Triangulo Isosceles")
])
def test_isosceles_permutation(a: int, b: int, c: int, tipo: str, triangule: Triangle):
    ret = triangule.check_triangle(a, b, c)
    assert ret == tipo


@pytest.mark.parametrize("a, b, c, tipo", [
    (5, 5, 0, "Não é um triângulo válido"),
    (7, 7, -2, "Não é um triângulo válido")
])
def test_invalid_value(a: int, b: int, c: int, tipo: str, triangule: Triangle):
    ret = triangule.check_triangle(a, b, c)
    assert ret == tipo


@pytest.mark.parametrize("a, b, c, tipo", [
    (8, 4, 4, "Não é um triângulo válido"),
    (8, 4, 4, "Não é um triângulo válido"),
    (4, 8, 4, "Não é um triângulo válido"),
    (4, 4, 8, "Não é um triângulo válido"),
])
def test_soma_dos_lados(a: int, b: int, c: int, tipo: str, triangule: Triangle):
    ret = triangule.check_triangle(a, b, c)
    assert ret == tipo


@pytest.mark.parametrize("a, b, c, tipo", [
    (8, 4, 4, "Não é um triângulo válido"),
    (8, 4, 4, "Não é um triângulo válido"),
    (4, 8, 4, "Não é um triângulo válido"),
    (4, 4, 8, "Não é um triângulo válido"),
])
def test_sum_of_2_sides_is_equalto_the_third_side(a: int, b: int, c: int, tipo: str, triangule: Triangle):
    ret = triangule.check_triangle(a, b, c)
    assert ret == tipo


@pytest.mark.parametrize("a, b, c, tipo", [
    (10, 4, 4, "Não é um triângulo válido"),
    (10, 4, 4, "Não é um triângulo válido"),
    (4, 10, 4, "Não é um triângulo válido"),
    (4, 4, 10, "Não é um triângulo válido"),
])
def test_the_sum_of_2_sides_is_less_than_the_third_side(a: int, b: int, c: int, tipo: str, triangule: Triangle):
    ret = triangule.check_triangle(a, b, c)
    assert ret == tipo


def test_all_values_are_zero(triangule: Triangle):
    ret = triangule.check_triangle(0, 0, 0)
    assert ret == "Não é um triângulo válido"