deuda = 40000
div = 12
pago = int(deuda / div)

def pago_recurente():
    print(f'Pago recurente de {pago}')
    for i in range(deuda, 0 - 1, -pago):
        print(f'Te restan {i}pesos')

pago_recurente()