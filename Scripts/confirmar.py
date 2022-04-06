from autenticarse import loguearse
import time
import requests
from reporte import meteteensap
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# excel = openpyxl.load_workbook("C:/Users/aalarcon/Desktop/osocna.xlsx")
# hoja = excel["osocna"]

def confirmar(fecha):

    token = loguearse()

    def confirmar(id_afip, punto_venta, factura, letra):
        letra_nueva = letra.strip()
        url_confirmar = "https://extranet.osocna.com.ar/Backend/api/ComprobantesExtranet/tipoComprobante/"+ str(id_afip) +"/puntoVenta/"+ str(punto_venta) +"/nroComprobante/"+ str(factura) +"/tipoEmision/"+ str(letra_nueva) +"/Confirmar"
        headers_confirmar = {"Authorization":token}
        payload = {}
        request = requests.post(url = url_confirmar, headers = headers_confirmar, data = payload, verify = False)

        response = request.text
        print(response, request.status_code)

    ## -- LISTAR NUEVAMENTE EL REPORTE CON LAS FACTURAS A CONFIRMAR -- ##
    factura_sap, fecha, puestoVenta, letra, facturas, caea, vto_caea, producto, unidades, iva, precio = meteteensap(0, "15.03.2022")

    cantidad = len(factura_sap)

    idAfip = None
    fact_rep = None

    i = 0
    for factura in facturas:
        print(factura)
        puesto_v = puestoVenta[i]
        _letra = letra[i]

        if factura == fact_rep:
            fact_rep = factura
            continue

        if puesto_v == "118":
            idAfip = 1
        elif puesto_v == "119":
            idAfip = 3

        confirmar(idAfip, puesto_v, factura, _letra)
        time.sleep(2)
        fact_rep = factura
        print("")
        i = i + 1
 
