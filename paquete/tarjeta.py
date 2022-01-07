# Funcion crear tarjeta
tarjeta = {}
def crear_tarjeta(nombre, card, tasa_interes, deuda_inicial, pago ):
    tarjeta ['Nombre'] = nombre
    tarjeta ['Tarjeta'] = card
    tarjeta ['Tasa de interes'] = tasa_interes
    tarjeta ['Deuda total'] = deuda_inicial
    tarjeta ['Pago mensual'] = pago
    return tarjeta

# Solicitud de datos del cliente
nombre = input('Nombre: ').title()
card = input('Tipo de tarjeta: ')
    # Calculo deuda inicial + interes mensual
tasa_interes = float(input('Tasa de interes: '))
deuda_inicial = int(input('Deuda inicial: '))
# deuda_total = round(deuda_inicial * (1 + tasa_interes/100), 2)
pago = int(input('Pago mensual: '))


if pago > deuda_inicial:
    print('Pago mayor a deuda \n Por favor ingrese de nuevo los datos')
else:
    print(crear_tarjeta(nombre, card, tasa_interes, deuda_inicial, pago))
    print('Gracias por tu pago')

# Funcion captura nueva deuda
def captura_nueva_deuda (tarjeta):
    deuda_recalculada = (deuda_inicial - pago)*(1 + (tasa_interes/12) / 100)
    tarjeta['Nueva deuda'] = deuda_recalculada
    for i in range(1):
        print(tarjeta)

captura_nueva_deuda(tarjeta)
nueva_deuda =  int(tarjeta['Nueva deuda'])

# Funcion generar reporte
def generar_reporte(tarjeta):
    print('Reporte: ')
    for i in tarjeta:
        print(i, ':', tarjeta[i])
generar_reporte(tarjeta)

# Iterar varias tarjetas.


# Funcion pago recurente
def pago_recurente():
    for i in range(nueva_deuda, -1, -pago):
        print(f'Te restan {i} pesos')
# pago_recurente()
