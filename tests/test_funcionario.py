import os
import sys
import pytest
from src.funcionarios import Funcionario, Cargo

cur_path = os.path.dirname(os.path.abspath(__file__))
head, _ = os.path.split(cur_path)
sys.path.insert(0, os.path.join(head, 'src'))

@pytest.fixture
def jim():
    return Funcionario("Jim Halpert", "jim@example.com", 3500, Cargo.DESENVOLVEDOR)

@pytest.fixture
def dwight():
    return Funcionario("Dwight Schrute", "dwight@example.com", 2500, Cargo.DBA)

@pytest.fixture
def pam():
    return Funcionario("Pam Beesly", "pam@example.com", 2500, Cargo.TESTADOR)

@pytest.fixture
def michael():
    return Funcionario("Michael Scott", "michael@example.com", 6000, Cargo.GERENTE)


def test_calcula_salario_desenvolvedor_maior_ou_igual_3000(jim):
    assert jim.calcular_salario_liquido() == 2800.0

def test_calcula_salario_desenvolvedor_menor_que_3000():
    jim = Funcionario("Jim Halpert", "jim@example.com", 2500, Cargo.DESENVOLVEDOR)
    assert jim.calcular_salario_liquido() == 2250.0

def test_calcula_salario_dba_maior_ou_igual_2000(dwight):
    assert dwight.calcular_salario_liquido() == 1875.0

def test_calcula_salario_dba_menor_que_2000():
    dwight = Funcionario("Dwight Schrute", "dwight@example.com", 1500, Cargo.DBA)
    assert dwight.calcular_salario_liquido() == 1275.0

def test_calcula_salario_testador_maior_ou_igual_2000(pam):
    assert pam.calcular_salario_liquido() == 1875.0

def test_calcula_salario_testador_menor_que_2000():
    pam = Funcionario("Pam Beesly", "pam@example.com", 1500, Cargo.TESTADOR)
    assert pam.calcular_salario_liquido() == 1275.0

def test_calcula_salario_gerente_maior_ou_igual_5000(michael):
    assert michael.calcular_salario_liquido() == 4200.0

def test_calcula_salario_gerente_menor_que_5000():
    michael = Funcionario("Michael Scott", "michael@example.com", 4000, Cargo.GERENTE)
    assert michael.calcular_salario_liquido() == 3200.0

if __name__ == "__main__":
    pytest.main()
