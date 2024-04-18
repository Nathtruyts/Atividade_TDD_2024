from enum import Enum

class Cargo(Enum):
    DESENVOLVEDOR = 1
    DBA = 2
    TESTADOR = 3
    GERENTE = 4

class Funcionario:
    def __init__(self, nome, email, salario_base, cargo):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo

    def calcular_salario_liquido(self):
        regras_salario = {
            Cargo.DESENVOLVEDOR: {True: 0.8, False: 0.9},
            Cargo.DBA: {True: 0.75, False: 0.85},
            Cargo.TESTADOR: {True: 0.75, False: 0.85},
            Cargo.GERENTE: {True: 0.7, False: 0.8}
        }
        limite_superior = {
            Cargo.DESENVOLVEDOR: 3000,
            Cargo.DBA: 2000,
            Cargo.TESTADOR: 2000,
            Cargo.GERENTE: 5000
        }
        
        limite = limite_superior[self.cargo]
        regra = regras_salario[self.cargo][self.salario_base >= limite]
        return self.salario_base * regra
