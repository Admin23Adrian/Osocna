import os, os.path
import win32com.client
import sys
import os
from getpass import getuser
from datetime import datetime
import win32com.client as win32
import pythoncom
from datetime import datetime
import subprocess
import time


def ingresarsap(usuario_sap, contrasena_sap):
    try:

        pythoncom.CoInitialize()
        path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        subprocess.Popen(path)
        time.sleep(2)

        SapGuiAuto = win32com.client.GetObject('SAPGUI')
        if not type(SapGuiAuto) == win32com.client.CDispatch:
            return

        application = SapGuiAuto.GetScriptingEngine
        if not type(application) == win32com.client.CDispatch:
            SapGuiAuto = None
            return
        connection = application.OpenConnection("ERP", True)

        if not type(connection) == win32com.client.CDispatch:
            application = None
            SapGuiAuto = None
            return

        session = connection.Children(0)
        if not type(session) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
            return
        time.sleep(1)
        #print(usuario_sap)
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = usuario_sap
        time.sleep(0.3)
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = contrasena_sap
        time.sleep(0.3)
        session.findById("wnd[0]").sendVKey(0)
        time.sleep(0.3)
        #time.sleep(0.5)
        #session.CreateSession()
        #time.sleep(0.5)
        #session.CreateSession()
        #time.sleep(0.5)
        #session.CreateSession()
    
    except:
        print(sys.exc_info()[0] + "Usuario y/o contraseña incorrecto. Vuelva a intentar.")

    finally:
        session = None
        connection = None
        application = None
        SapGuiAuto = None


def meteteensap(sesionsap, fecha):
        pythoncom.CoInitialize()

        SapGuiAuto = win32com.client.GetObject('SAPGUI')
        if not type(SapGuiAuto) == win32com.client.CDispatch:
            return

        application = SapGuiAuto.GetScriptingEngine
        if not type(application) == win32com.client.CDispatch:
            SapGuiAuto = None
            return
        connection = application.Children(0)

        if not type(connection) == win32com.client.CDispatch:
            application = None
            SapGuiAuto = None
            return

        session = connection.Children(sesionsap)
        if not type(session) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
            return


        session.findById("wnd[0]").maximize()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nz_sd_detalle_factura"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/radLOTE_NO").select()
        session.findById("wnd[0]/usr/ctxtSO_FECHA-LOW").text = fecha
        session.findById("wnd[0]/usr/ctxtSO_FECHA-HIGH").text = fecha
        session.findById("wnd[0]/usr/ctxtP_SOLICI").text = "20000041"
        session.findById("wnd[0]/usr/radLOTE_NO").setFocus()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/tbar[1]/btn[33]").press()
        session.findById("wnd[1]/usr/ssubD0500_SUBSCREEN:SAPLSLVC_DIALOG:0501/cntlG51_CONTAINER/shellcont/shell").setCurrentCell(171,"TEXT")
        session.findById("wnd[1]/usr/ssubD0500_SUBSCREEN:SAPLSLVC_DIALOG:0501/cntlG51_CONTAINER/shellcont/shell").firstVisibleRow = 162
        session.findById("wnd[1]/usr/ssubD0500_SUBSCREEN:SAPLSLVC_DIALOG:0501/cntlG51_CONTAINER/shellcont/shell").selectedRows = "171"
        session.findById("wnd[1]/usr/ssubD0500_SUBSCREEN:SAPLSLVC_DIALOG:0501/cntlG51_CONTAINER/shellcont/shell").clickCurrentCell()
                

        # myGrid = session.findById("wnd[0]/usr/cntlCONTAINER/shellcont/shell")
        myGrid = session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell")
        

        factura_sap = []
        fe_fact = []
        puesto_venta = []
        letra = []
        factura = []
        caea = []
        vto_caea = []
        producto = []
        unidades = []
        iva = []
        precio = []

        time.sleep(0.4)

        for i in range(0,600):
            try:
                factura_sap.append(myGrid.getCellValue(i, "N_FACT_SAP"))
                fe_fact.append(myGrid.getcellvalue(i,"FKDAT"))
                puesto_venta.append(myGrid.getcellvalue(i,"PUESTO_V"))
                letra.append(myGrid.getcellvalue(i,"LETRA_FAC"))
                factura.append(myGrid.getcellvalue(i, "N_FACTURA"))
                caea.append(myGrid.getcellvalue(i,"CAI"))
                vto_caea.append(myGrid.getcellvalue(i,"VTO_CAI"))
                producto.append(myGrid.getcellvalue(i,"ZZTXT"))                
                iva.append(myGrid.getcellvalue(i,"IVA"))   
                precio.append(myGrid.getcellvalue(i,"PREC_UNIT"))   
                unidades.append(myGrid.getcellvalue(i,"FKIMG"))
                
            except:
                break
        
        return factura_sap, fe_fact, puesto_venta, letra, factura, caea, vto_caea, producto, unidades, iva, precio


# ingresarsap("aalarcon", "Adrian2020")
# resultados = meteteensap(0, "15.04.2020")
# stringCantidades = resultados[8]
# stringFecha = "2020-04-15"
# fechaDateTime = datetime.strptime(stringFecha, "%Y-%m-%d")
# print(fechaDateTime.date())

# intCantidades = list(map(int, stringCantidades))
# print(intCantidades)

