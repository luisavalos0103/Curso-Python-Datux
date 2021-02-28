
# Pirámide de Mario

alt = input("Ingrese la altura de la pirámide (entre 1 y 8): ")

if not alt.isnumeric():
    print("Inválido!, Vuelva a ingresar la altura por favor")
elif int(alt) < 1 or int(alt) > 8:
    print("Inválido!, Vuelva a ingresar la altura por favor")
else:
    for i in range(int(alt)):
        print(" " * (int(alt)-i-1) + "#" * (i+1))