numeros_decrescentes = []
for num in range(3):
    num = int(input(f'Digite um valor para {num + 1}: '))
numeros_decrescentes.append(num)
numeros_decrescentes.sort(reverse=True)
print(numeros_decrescentes)
