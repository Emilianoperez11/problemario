sueldo = (float(input("ingrese su sueldo")))
anosdeantiguedad = (float(input("ingrese los anos de antiguedad")))

if anosdeantiguedad <5:
    porcentajedeantiguedad = 0.30

else :
    porcentajedeantiguedad = 0.50

sueldo_a_cobrar = (sueldo + (sueldo * anosdeantiguedad))

print(sueldo_a_cobrar)
