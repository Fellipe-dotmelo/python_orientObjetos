class Equipamento:
    def __init__(self, marca, preco, ano_fab):
        self.__marca = marca
        self.__preco = preco
        self.__ano_fab = ano_fab

    def get_marca(self):
        return self.__marca

    def get_preco(self):
        return self.__preco

    def set_preco(self, ano):
        self.__ano_fab = ano

    def get_ano_fab(self):
        return self.__ano_fab

    def ligar(self):
        print(f"O equipamento da marca {self.__marca}, pode ser ligado!")

    def funcionar(self):
        print("Este equipamento pode funcionar!")