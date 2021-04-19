import requests
import sys
import os
import time
import openpyxl
from openpyxl import load_workbook
from autenticarse import loguearse

token = loguearse()

def carga_factura(factura, pdf, tipo_comprob, punto_venta, letra, ruta_pdf):
    letraNueva = letra.strip()
    url_pdf = "https://extranet.osocna.com.ar/Backend/api/ComprobantesExtranet/tipoComprobante/"+str(tipo_comprob)+"/puntoVenta/"+str(punto_venta)+"/nroComprobante/"+str(factura)+"/tipoEmision/"+str(letraNueva)+"/PDFComprobante"
    headers_pdf = {"Authorization": token}
    factura_pdf = {"archivo": (pdf, open(ruta_pdf, "rb"), "application/pdf")}
    # print(url_pdf)
    solicitud = requests.post(url = url_pdf, headers = headers_pdf, files = factura_pdf)
    print(f"Status carga factura: {solicitud.status_code}")




def adjuntos(ruta, tipo_comprob, punto_venta, letra, factura):
    letraNueva = letra.strip()
    url_adjuntos = "https://extranet.osocna.com.ar/Backend/api/ComprobantesExtranet/tipoComprobante/"+str(tipo_comprob)+"/puntoVenta/"+str(punto_venta)+"/nroComprobante/"+str(factura)+"/tipoEmision/"+str(letraNueva)+"/Adjuntos"
    # print(url_adjuntos)
    headers_adjuntos = {"Authorization": token}
    lista_carpetas_adjuntos = os.listdir(ruta)

    # iterar las carpetas Presupuesto, Remitos, OC: carpeta es cada una de ellas
    for carpeta in lista_carpetas_adjuntos:
        ruta_cda_carpeta = ruta + "/" + carpeta
        if os.path.isdir(ruta_cda_carpeta) == True:
            contenido_carpeta = os.listdir(ruta_cda_carpeta)
            if contenido_carpeta != [] and carpeta == "Presupuestos":
                for presup in contenido_carpeta:
                    presupuesto = f"{ruta_cda_carpeta}/{presup}" # ruta del pdf presupuesto
                    nuevo_presupuesto = f"{ruta_cda_carpeta}/PR{presup}"
                    os.rename(presupuesto, nuevo_presupuesto)
                    time.sleep(1)
            # Adjuntos de cada carpeta
            adjuntos_modificados = os.listdir(ruta_cda_carpeta)
            if adjuntos_modificados != []:
                for presupuesto_mod in adjuntos_modificados:
                    # print("Ruta carpetas: ", ruta_cda_carpeta)
                    ruta_adjunto = ruta_cda_carpeta + "/" + presupuesto_mod
                    # print(ruta_adjunto)
                    adjunto_a_subir = {"archivo": (presupuesto_mod, open(ruta_adjunto, "rb"), "application/pdf")}
                    
                    request = requests.post(url = url_adjuntos, headers = headers_adjuntos, files = adjunto_a_subir)
                    print(f"Status de Subir Adjuntos: {request.status_code}")
                    


def recorrer_carpetas(factura, tipoCompr, punto_vent, letra):
    pv = punto_vent
    print("Factura a subir: ", factura)
    carpeta_legajos = "C:/Users/aalarcon/Desktop/20000041"
    carpeta_madre = os.listdir(carpeta_legajos)
    # Nombre de la carpeta de la factura que se consulta actualmente.
    carpeta_factura = f"00{pv}A00{factura}"

    for cda_carpeta in carpeta_madre:
        
        if cda_carpeta == carpeta_factura:
            # print(cda_carpeta)
            ruta_contenido_factura = f"{carpeta_legajos}/{carpeta_factura}"
            contenido_factura = os.listdir(ruta_contenido_factura)
            for contenido in contenido_factura:
                if contenido.endswith(".pdf"):
                    print(f"Factura en pdf: {contenido}")
                    ruta_pdf_contenido = f"{ruta_contenido_factura}/{contenido}" 
                    # llamada a la funcion
                    carga_factura(factura, contenido, tipoCompr, punto_vent, letra, ruta_pdf_contenido)
                    adjuntos(ruta_contenido_factura, tipoCompr, punto_vent, letra, factura)
                else:
                    break

        else:
            continue        
            