totalcuenta = input('total  de cuenta  es:$')
totalcuenta = totalcuenta.replace('.', '')
totalcuenta = int(totalcuenta)
porcentaje_propina  = int(input('porcentaje de propina (ej:10%,15%,20%:'))
montopropina = totalcuenta * (porcentaje_propina / 100)
totalpago = totalcuenta + montopropina
print (f"el total de cuenta es:$ {totalcuenta:,}.")
print (f"Propina:$ {montopropina:,}.")
print (f"el total de su cuenta es:$ {totalpago:,}.")
