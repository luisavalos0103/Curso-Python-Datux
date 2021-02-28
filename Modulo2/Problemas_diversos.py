### Problemas diversos

# Ejercicio 1

def ingresar_nota():
    
    try:
        nota = float(input("Introduce la nota(0 - 10): "))
        
        if nota >=0 and nota <= 10:
            return nota  # Importante romper la iteración si todo ha salido bien
        else:
            print('Nota fuera del rango')
            ingresar_nota()
    except:
        print("Ha ocurrido un error, introduzca correctamente la nota")
        ingresar_nota()
        
def listar_alumnos(cantidad_alumnos):
    lista_alumnos = []
    for i in range(cantidad_alumnos):
        alumno = {}
        # Ingreso de nombre de alumno
        alumno['nombre'] = input('Ingrese el nombre del alumno {}: '.format(i+1))
    
        # ingreso de notas
        alumno['nota1'] = ingresar_nota()
        alumno['nota2'] = ingresar_nota()
        alumno['nota3'] = ingresar_nota()
    
        # agregando alumno a lista alumnos
        lista_alumnos.append(alumno)
    
    return lista_alumnos

n = int(input('Cantidad de alumnos a ingresar: '))
listado = listar_alumnos(n)
listado

# Ejercicio 2

def aprobaron():
    m = int(input("Ingrese el numero de alumnos: "))
    listado = listar_alumnos(m)
    c=0
    for i in range(m):
        n1 = listado[i]['nota1']
        n2 = listado[i]['nota2']
        n3 = listado[i]['nota3']
        Prom = (n1+n2+n3)/3
        if Prom < 4:
            c+=1
    print("La cantidad de aprobados es: {}".format(m-c))
    
aprobaron()

# Ejercicio 3

def promedio_curso(n):
    listado = listar_alumnos(n)
    c=0
    S=0
    Promedio=[]
    for i in range(n):
        
        n1 = listado[i]['nota1']
        n2 = listado[i]['nota2']
        n3 = listado[i]['nota3']
        Prom = (n1+n2+n3)/3
        Promedio.append(Prom)
        
    for j in Promedio:
        S = S + j 
        
    
    Total = S / n

    
    print("El promedio del curso es: {0:.3f}".format(Total))
    
promedio_curso(2)


# Ejercicio 4

def promedio_max_min(n):
    listado = listar_alumnos(n)
    c=0
    Promedio=[]
    for i in range(n):
        
        n1 = listado[i]['nota1']
        n2 = listado[i]['nota2']
        n3 = listado[i]['nota3']
        Prom = (n1+n2+n3)/3
        Promedio.append(Prom)
        
    maximo=max(Promedio)
    minimo=min(Promedio)
    a=Promedio.index(maximo)
    b=Promedio.index(minimo)
    
    print("El promedio más alto fue de: {}".format(listado[a]['nombre']))
    print("El promedio más bajo fue de: {}".format(listado[b]['nombre']))
        
promedio_max_min(2)

# Ejercicio 5

print(listado)

for i in range(len(listado)):
        
        n1 = listado[i]['nota1']
        n2 = listado[i]['nota2']
        n3 = listado[i]['nota3']
        prom = round((n1+n2+n3)/3,3)
        listado[i]['Promedio'] = prom

listado


def Busqueda(texto):
    try:
        for i in range(3):
            if texto == listado[i]['nombre']:
                print(listado[i])
    except:    
        print("No se ha encontrado alumnos con ese nombre:")
            
Busqueda("lucas")


