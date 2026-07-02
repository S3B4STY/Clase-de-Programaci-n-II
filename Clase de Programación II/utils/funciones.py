from datetime import datetime

def obtener_fecha():
    return datetime.now().strftime("%d/%m/%Y")

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_iva(subtotal, porcentaje=15):
    return subtotal * porcentaje / 100

def calcular_total(subtotal, iva):
    return subtotal + iva
