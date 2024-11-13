menor_10 = 0
entre_10y100 = 0
mayor_100 = 0
negativo = 0
igual_0 = 0

for i in range(100):
    numero = float(input(f"ingrese el valor {i+1}:"))

if numero > 0 and numero < 10:
    menor_10 += 1
    print(f"valores mayor a 0 y menores a 10:{menor_10}")
elif 10 <= numero <= 100:
    entre_10y100 += 1
    print(f"valores entre 10 y 100:{entre_10y100}")
elif numero > 100:
    mayor_100 += 1
    print(f"valores mayores a 100:{mayor_100}")
elif numero < 0:
    negativo += 1
    print(f"valores negativos:{negativo}")
elif numero == 0:
    igual_0 += 1
    print(f"valores iguales a 0:{igual_0}")
