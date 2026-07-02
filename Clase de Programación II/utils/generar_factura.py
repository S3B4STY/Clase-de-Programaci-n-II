from utilidades.funciones import (
    calcular_subtotal,
    calcular_iva,
    calcular_total,
    obtener_fecha
)

def generar_factura(cliente, producto, precio, cantidad):
    subtotal = calcular_subtotal(precio, cantidad)
    iva = calcular_iva(subtotal)
    total = calcular_total(subtotal, iva)

    factura = f"""
==============================
          FACTURA
==============================
Fecha: {obtener_fecha()}
Cliente: {cliente}

Producto : {producto}
Cantidad : {cantidad}
Precio   : ${precio:.2f}

Subtotal : ${subtotal:.2f}
IVA      : ${iva:.2f}
TOTAL    : ${total:.2f}
==============================
"""

    return factura
