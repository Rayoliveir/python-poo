from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Endereco:
    def __init__(self, longradouro: str, numero: int, complemento: str, cep: str, cidade: str) -> None:
        self.longradouro = longradouro
        self.numero = numero
        self.complemeto = complemento
        self.cep = cep
        self.cidade = cidade

    def exibir_endereco(self) -> str:
            return f"\nLongradouro: {self.longradouro} \nNumero: {self.numero} \nComplemento: {self.complemeto} \nCEP: {self.cep} \nCidade: {self.cidade}"

        

class Funcionario(ABC):
    # Constructor
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def calcular_salario():
        pass

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def calcular_salario():
          pass

class Medico(Funcionario):
     def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
        
     def calcular_salario():
          pass