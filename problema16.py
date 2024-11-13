suma = 0
contador = 0

for i in range(10):
    numero = float(input(f"ingresa un valor {i+1}:"))
if 5 <= numero <= 2500 :
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"el promedio de los valores compredidos entre 5 y 2500 es:{promedio:.2f}")
else:
    print("No se ingresaron valores comprendidos entre 5 y 2500 ")
