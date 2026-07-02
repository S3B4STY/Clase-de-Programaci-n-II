def validar_nombre(nombre):
    return len(nombre.strip()) > 0

def validar_precio(precio):
    return precio > 0

def validar_cantidad(cantidad):
    return cantidad > 0
