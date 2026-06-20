
print(5+6)

print(10%3)#modulo o residuo

print(5**3) #potencia

print(10//3) #division entera

print(5/2) #division normal

#variables puede ser tipo nombre, Nombre, nombre3, nombre_3, _nombre, pero no pueden empezar con un numero ni contener espacios ni caracteres especiales
#la variable viene definida por el contenido.
#en python todo es un objeto

nombre=5
print(type(nombre)) #clase int

Nombre="Juan"
print(type(Nombre)) #clase str

nombre1=3.14
print(type(nombre1)) #clase float, float en ingles es decimal

mensaje="""Este es un mensaje
con tres saltos
de linea"""
print(mensaje)


numero1=5   
numero2=7
if numero1>numero2:
    print("numero 1 es mayor que numero 2")
else:
    print("numero 2 es mayor que numero 1")

    # = es asignacion y == es comparacion, el primer caso asigna un valor a una variable, el segundo caso compara dos valores y devuelve un booleano (True o False) dependiendo del resultado de la comparacion.
