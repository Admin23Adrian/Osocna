import requests
from autenticarse import loguearse
import json

token = loguearse()


def altaDocs(letra, puestoVenta, nroFact, fecha, nroCaea, descripcion, lineas_externas, id_afip, idalicuota, alicuota):
    
    mijson = {
            "idMoneda": 1,
            "tipoCambio": 1,
            "idTipoComprobanteAfip": int(id_afip),
            "puntoVenta": int(puestoVenta),
            "nroComprobante": int(nroFact),
            "fechaComprobante": fecha,
            "tipoEmision": "E",
            "nroAutorizacion": 123456789,
            "fechaVencimiento": fecha,
            "vencimientoAutorizacion": fecha,
            "descripcion": descripcion,
            "lineas": [
                {
                    "idAlicuota": int(idalicuota),
                    "cantidad": 1,
                    "importeNeto": 2000,
                    "descripcion": "medicamentos sin iva"
                }
            ],
            "tributos": [
                {
                    "idTributo": 99,
                    "alicuota": int(alicuota),
                    "importeImponible": 1
                }
            ]
    }
    # print(nroCaea)
    # print(mijson)
    mijson["lineas"] = lineas_externas
    json_fecha = json.dumps(mijson, default=str)
    json_final = json.loads(json_fecha)
    
    urlCons = "https://extranet.osocna.com.ar/BackEnd/api/ComprobanteExtranet"
    headers = {"Authorization":token}

    response = requests.post(url=urlCons, headers=headers, json=json_final)
    print("Alta de documentos: ",response.status_code, response.text)