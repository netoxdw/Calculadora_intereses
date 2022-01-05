# Funcion crear tarjeta
def crear_tarjeta(nombre, card, tasa_interes, deuda1, pago ):
    tarjeta = {}
    tarjeta ['Nombre'] = nombre
    tarjeta ['Tarjeta'] = card
    tarjeta ['Tasa de interes'] = tasa_interes
    tarjeta ['Deuda inicial'] = deuda1
    tarjeta ['Monto a pagar'] = pago
    return tarjeta

nombre = input('Nombre: ').title()
card = input('Tipo de tarjeta: ')
tasa_interes = float(input('Tasa de interes: '))
deuda1 = int(input('Deuda inicial: '))
pago = int(input('Monto a pagar: '))

print(crear_tarjeta(nombre, card, tasa_interes, deuda1, pago))

