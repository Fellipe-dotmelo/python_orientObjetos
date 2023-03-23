class Conta:
    def __init__(self,titular, limite, saldo, numero):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        print(f"A conta de numero {self.__numero} do cliente {self.__titular} tem R$ {self.__saldo} em saldo com limite de {self.__limite}")

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)
        print(f'O valor foi transferido com sucessso para a conta do {destino.__titular}')

    @staticmethod
    def banco():
        return "Banco do Brasil"