from datetime import datetime

def convertir_fecha(fecha):
    string_fecha = fecha.strip()
    
    dia = fecha[0:2]
    mes = fecha[3:5]
    anio = fecha[6:]

    fecha_nueva = f"{anio}/{mes}/{dia}"
    objeto_fecha = datetime.strptime(fecha_nueva, '%Y/%m/%d')
    return objeto_fecha.date()
    

# fe_conver = convertir_fecha("15.04.2020")
# print(f"Fecha convertida: {fe_conver}")
# print(type(fe_conver))