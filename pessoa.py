import time
class Pessoa:
    def __init__(self, nome, cpf, dt_nascim, email, cidade, estado):
        self.__nome = nome.title()
        self.__nome2 = nome.title()
        self.__cpf = cpf
        self.__dt_nascim = dt_nascim
        self.__email = email
        self.cidade = cidade
        self.estado = estado

    @property
    def nome2(self):
        return self.__nome2

    @nome2.setter
    def nome2(self, nome):
        self.__nome2 = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome.title()

    def get_cpf(self):
        return self.__cpf

    def get_dt_nascim(self):
        return self.__dt_nascim

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def andar(self):
        print("Você pode andar e até mesmo correr!")

    def falar(self):
        print("Você pode falar, mas tome cuidado com a sua lingua!")

    def trabalhar(self):
        print(f"Parabéns {self.__nome} , você pode trabalhar para ter dinheiro!")

    def trabalhar2(self):
        print(f"Parabéns {self.nome2} , você pode trabalhar para ter dinheiro!")


    def soletrar(self):
        for l in self.__nome:
            time.sleep(0.5)
            print(l, end="  ")

    def dormir(self):
        for l in "zzzzz":
            time.sleep(0.5)
            print(l, end="  ")