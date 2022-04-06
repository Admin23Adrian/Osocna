from autenticarse import loguearse
from altaDocumentos import altaDocs
from escanearPDFs import recorrer_carpetas
import time
from reporte import meteteensap
from fechas import convertir_fecha
from conversionImportes import conversionMoneda, convertiIva
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def envio_documentacion(fecha):

    lineasDup = []
    lineasNorm = []

    factura_sap, fecha, puestoVenta, letra, facturas, caea, vto_caea, producto, unidades, iva, precio = meteteensap(0, "15.03.2022")

    n = 0
    c = 0

    for f in facturas:
        # Variables.
        descripcion_medicamento = ""
        id_afip = None
        idalicuota = None
        alicuota = None
        importeStr = precio[n]
        ivaNum = convertiIva(iva[n])

        # Se convierte la fecha de tipo string de sap a formato datetime
        fecha_convertida = convertir_fecha(fecha[n])
        # Se convierte el precio de sap a formato float para que la pagina tome bien el precio.
        importe = conversionMoneda(importeStr)
        # print(importe, type(importe))

        # Se asigna la descripcion del medicamento dependiendo el puesto de venta y si tiene producto asignado.
        if (puestoVenta[n] == "118" or puestoVenta[n] == "45" or puestoVenta[n] == "88") and producto[n] != None:
            descripcion_medicamento = "Medicamentos"
            # Se declara un id afip.
            id_afip = 1
        elif puestoVenta[n] == "118" and producto[n] == None:
            descripcion_medicamento = "Servicios"
            # Se declara un id afip.
            id_afip = 1
        elif puestoVenta[n] == "119" and producto[n] == None:
            descripcion_medicamento = "Nota de credito servicios"
            # Se declara un id afip.
            id_afip = 3
        elif puestoVenta[n] == "119" and producto[n] != None:
            descripcion_medicamento = "Nota de credito medicamentos"
            # Se declara un id afip.
            id_afip = 3

        # Se define un numero de alicuota alicuota.
        if ivaNum == 21.0:
            # print("Coincide ivaNum con 21.0")
            idalicuota = 5
        else:
            idalicuota = 3

        # Esta parte es la logica para las facturas duplicadas que deben ir como varios json en una lista.
        # Tambien esta parte es la que decide en que momento dar de alta el comprobante. (LINEA 74)
        factRepetida = facturas.count(f)
        if factRepetida > 1:
            c = c + 1
            json = {
                "idAlicuota": idalicuota,
                "cantidad": unidades[n],
                "importeNeto": importe,
                "descripcion": producto[n]
            }
            lineasDup.append(json)
            if c == factRepetida:
                altaDocs(letra[n], puestoVenta[n], facturas[n], fecha_convertida, caea[n], descripcion_medicamento, lineasDup, id_afip, idalicuota, ivaNum)
                recorrer_carpetas(facturas[n], id_afip, puestoVenta[n], letra[n])
                print("")
                # print(lineasDup)
                c = 0
                lineasDup.clear()

        else:
            json2 = {
                "idAlicuota": idalicuota,
                "cantidad": unidades[n],
                "importeNeto": importe,
                "descripcion": producto[n]
            }
            lineasNorm.append(json2)
            altaDocs(letra[n], puestoVenta[n], facturas[n], fecha_convertida, caea[n], descripcion_medicamento, lineasNorm, id_afip, idalicuota, ivaNum)
            recorrer_carpetas(facturas[n], id_afip, puestoVenta[n], letra[n])
            print("")
        time.sleep(3)

        lineasNorm.clear()

        n += 1

        # Se agrega facturas 88 + 45

    
        
        
    



