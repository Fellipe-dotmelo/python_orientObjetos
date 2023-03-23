def criar_conta(titular, numero, limite, saldo):
    return {"titular": titular, "numero": numero, "limite": limite, "saldo": saldo}

def depositar(conta, valor):
    if(valor >= 150):
        valor += valor * 0.01
    conta['saldo'] += valor

def sacar(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f"A conta de numero {conta['numero']} do cliente {conta['titular']} tem R$ {conta['saldo']} em saldo")



