

def convertiIva(strIva):
    iva = strIva
    cont = 0
    if iva != "0,00":
        for car in iva:
            if car == ",":
                ivaAux = iva.replace(",", "")
        for car2 in ivaAux:
            if car2 == "0":
                ivaAux2 = ivaAux.replace("0", "")
    else:
        niva = float(iva.replace(",", "."))
        return niva
    return float(ivaAux2)




def conversionMoneda(monedaStr):
    cambio1 = str(monedaStr)
    for car in monedaStr:
        if car == ".":
            cambio1 = monedaStr.replace(".", "")
            break
    
    # print(cambio1)
    cambio2 = cambio1.replace(",", ".")
    # print(cambio2)
    monedaFinal = float(cambio2)
    # print(monedaFinal)

    return monedaFinal

# moneda = conversionMoneda("21,00")
# print(moneda, "Tipo:", type(moneda))

# print(convertiIva("0,00"))
# print(float("0.00"))