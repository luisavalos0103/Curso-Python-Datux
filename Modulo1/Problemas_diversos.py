### Problemas diversos ########

## Ejercicio 1 

deposito = float(input("Ingrese el monto a depositar: "))

saldo_1a = deposito*1.04
saldo_2a = saldo_1a*1.04
saldo_3a = saldo_2a*1.04

print("Tras el primer año, Ud habrá acumulado: {0:.2f}".format(saldo_1a))
print("Tras el segundo año, Ud habrá acumulado: {0:.2f}".format(saldo_2a))
print("Tras el tercer año, Ud habrá acumulado: {0:.2f}".format(saldo_3a))


### Ejercicio 2

a = float(input("Ingrese coeficiente a:"))
b = float(input("Ingrese coeficiente b:"))
c = float(input("Ingrese coeficiente c:"))

discriminante = b**2 - 4 * a * c
if discriminante >= 0:
    if discriminante == 0:
        x = -b / (2 * a)
        print("La raíz única es {:.3f}".format(x))
    else:
        x1 = (-b + (discriminante)**(1/2)) / (2 * a)
        x2 = (-b - (discriminante)**(1/2)) / (2 * a)
        print("La raíz real x1 es {:.3f}".format(x1))
        print("La raíz real x2 es {:.3f}".format(x2))
else:
    discriminante = abs(discriminante)
    parteReal = -b / (2 * a)
    parteImaginaria = (discriminante)**(1/2) / (2 * a)
    print("La raíz compleja x1 es {:.3f} + {:.3f}i".format(parteReal, parteImaginaria))
    print("La raíz compleja x2 es {:.3f} - {:.3f}i".format(parteReal, parteImaginaria))
