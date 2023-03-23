from conta import Conta
from pessoa import Pessoa
from equipamento import Equipamento

'''pessoa = Pessoa("jose wilton", "978987", "10/10/1999", "emial@test.com", "Brasilia","DF")
print(pessoa.nome2)
pessoa.nome2 = "novo nome"

pessoa.trabalhar2()

print(pessoa.nome2)

pessoa.set_nome("jose wilton souza")
print(pessoa.get_nome())'''

'''
furadeira = Equipamento("Philips","12.99", 2021)

print(furadeira.get_preco())
furadeira.ligar()
furadeira.funcionar()
'''
conta = Conta("Mozart",1000.0,83.0,332)
conta.extrato()
conta.depositar(90)
conta.depositar(1800)
conta.depositar(8)
conta.extrato()
print(conta.banco())
conta.sacar(3500)
#novo_limite = float(input("Informe o novo limite: "))
#conta.set_limite(novo_limite)
conta.extrato()

conta2 = Conta("Jucicleide",1000.0,90.0,332)
print(Conta.banco())



'''from funcao_conta import criar_conta, depositar, sacar, extrato

conta_mozart = criar_conta("Mozart",332,1000.0, 654.0)
conta_alan = criar_conta("Alan", 551, 1000.0, 1500.0)
conta_jean = {"titular": "Jean", "saldo": 750.0}

depositar(conta_jean, 100)

extrato(conta_jean)

depositar(conta_mozart, 150)
depositar(conta_alan, 1100)
sacar(conta_alan, 899)

extrato(conta_alan)'''
