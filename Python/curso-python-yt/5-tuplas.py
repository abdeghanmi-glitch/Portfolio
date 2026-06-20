#las tuplas son listas inmutables, es decir, no se pueden modificar una vez creadas. Se definen utilizando paréntesis () y pueden contener elementos de diferentes tipos de datos.
#una tupla se ejecuta mas rapido que una lista, por lo que es recomendable utilizar tuplas cuando no se necesite modificar los datos.
#sintaxis: tupla = (elemento1, elemento2, elemento3, ...), empieza en 0, 
#se puede acceder a los elementos de la tupla utilizando el indice del elemento, por ejemplo: tupla[0] devuelve el primer elemento de la tupla.

mituplaa=("Juan", 13, 1, 1995) 
milista=list(mituplaa) #convertimos la tupla en una lista para poder modificarla
print(mituplaa[1])
print(milista)

mitupla=tuple(milista) #convertimos la lista de nuevo en una tupla

print("Juan" in mitupla) #verificamos si un elemento esta en la tupla, devuelve True o False

print(mitupla.count(13)) #contamos cuantas veces se repite un elemento en la tupla

print(len(mitupla)) #obtenemos la longitud de la tupla

mitupla2=("Maria",)
print(len(mitupla2)) #obtenemos la longitud de la tupla, en este caso es 1, ya que solo tiene un elemento

mitupla3="Evil", 13, 1, 1995 #otra forma de definir una tupla sin utilizar paréntesis, pero es recomendable utilizar paréntesis para evitar confusiones
nombre, dia, mes, anio=mitupla3 #desempaquetamos la tupla en variables individuales
print(nombre)