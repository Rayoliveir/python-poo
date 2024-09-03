import os
os.system("cls || clear") # Limpa o terminal

class SaldoInsuficienteError(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 # Atributo protegido

    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor) -> float:
        # try - except
        try: 
            self.__verificar_sacar(valor)
        except SaldoInsuficienteError as error:
            return f"Erro: {error}"

        
        self._saldo -= valor
        return self._saldo
    
    def __verificar_sacar(self, valor): # etodo privado
        if valor > self._saldo:
            raise  SaldoInsuficienteError("Saldo insuficiente") # Lançando um erro
        
    def depositar(self, valor):
        self._saldo += valor
        return self._saldo

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

# Instanciando classes
conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaPoupanca(444, 555)

print(conta_corrente._saldo)
print(conta_corrente.sacar(200))
print(conta_corrente._saldo)
