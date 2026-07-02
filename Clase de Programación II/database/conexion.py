from openpyxl import load_workbook

def abrir_excel(nombre_archivo):

    ruta = f"database/{nombre_archivo}"

    libro = load_workbook(ruta)

    hoja = libro.active

    return libro, hoja
