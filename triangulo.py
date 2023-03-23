'''1. Classe Triangulo: Crie uma classe que modele um triangulo:
– Atributos: LadoA, LadoB, LadoC
– Métodos: calcular Perímetro, getMaiorLado;
Crie um programa que utilize esta classe.
Ele deve pedir ao usuário que informe as medidas de um triangulo.
Depois, deve criar um objeto com as medidas e imprimir sua área e maior lado.'''

class Triangulo:
    def __int__(self, ladoA, ladoB, ladoC):
        self.__ladoA = ladoA
        self.__ladoB = ladoB
        self.__ladoC = ladoC

    def calcPerimetro(self):
        return self.__ladoA + self.__ladoB + self.__ladoC

    def getMaiorLado(self):
        return max(self.__ladoA, self.__ladoB, self.__ladoC)

ladoA = float(input("Informe o valor de A do triângulo: "))
ladoB = float(input("Informe o valor de A do triângulo: "))
ladoC = float(input("Informe o valor de A do triângulo: "))

triangulo = Triangulo(ladoA, ladoB, ladoC)

print(f'O perímetro do triânglo informado é de: {triangulo.calcPerimetro()}')
print(f'O maior lado do triângulo informado é o: {triangulo}, com {triangulo.getMaiorLado()} lados')