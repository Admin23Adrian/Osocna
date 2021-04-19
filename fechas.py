from datetime import datetime

def convertir_fecha(fecha):
    string_fecha = fecha.strip()
    encuentra_punto = string_fecha.find(".")

    if encuentra_punto >= 1:
        nueva_fecha = string_fecha.replace(".", "/")
        fecha_dt = datetime.strptime(nueva_fecha, '%d/%m/%Y')
    return fecha_dt

# fe_conver = convertir_fecha("15.04.2020")
# print(f"Fecha convertida {fe_conver}")