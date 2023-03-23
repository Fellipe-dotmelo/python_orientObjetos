from funcao_conta import criar_conta, depositar

conta = criar_conta(input("Informe o seu nome: "), int(input("Informe o número de sua conta: ")), int(input("Informe o seu limite: ")),
                    int(input("Informe o seu saldo: ")))

depositar(conta, 110)

print(f"A conta de {conta['titular']}, de númeração {conta['numero']}, com limite {conta['limite']} e um saldo de {conta['saldo']}")