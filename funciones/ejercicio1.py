def total_factura(pago, iva):
    if iva != 0:
        resultado = pago - ((iva/100)*(pago))
        return resultado
    else:
        return pago - ((0.79)*(pago))

#def main():
pago = float(input("Ingresa la cantidad de pago sin el porcentaje de IVA: "))
iva = float(input("Ingresa tu porcentaje de IVA: "))
    
pago_total = total_factura(pago, iva)
    
print(f"Pago total: {pago_total}")