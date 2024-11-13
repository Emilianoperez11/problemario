primernum = float(input("ingrese el primer numero"))
segundonum = float(input("ingrese el segundo numero"))
tercernum = float(input("ingrese tercer numero "))

if primernum >= segundonum and primernum >= tercernum :
    mayor = primernum
    print(primernum)

elif segundonum >= primernum and segundonum >= tercernum :
    mayor = segundonum
    print(segundonum)
else :
    mayor = tercernum
    print(tercernum)
