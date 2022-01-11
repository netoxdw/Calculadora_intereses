from tarjeta import generar_reporte
lista = []
t1 = {'Nombre': 'Juan', 'Tarjeta': 'oro', 'Tasa de interes': 10, 'Deuda': 50000, 'Monto de pago': 4500, 'Nueva deuda': 45500}


lista.append(t1)


def multiples_reportes(lista):
    for tarjeta in lista:
        print(generar_reporte(tarjeta))
multiples_reportes(lista)
