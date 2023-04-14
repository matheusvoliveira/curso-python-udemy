def criaConta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta
conta = criaConta(123, 'Nico', 55.0, 1000.0 )
print(conta['numero'])
#teste

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print('saldo é {}.'.format(conta['saldo']))

criaConta(123, "Nico", 55.0, 1000.0)
deposita(conta, 15.0)
print(extrato(conta))
saca(conta, 20.0)
print(extrato(conta))
