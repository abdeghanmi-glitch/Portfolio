#Los diccionarios son una estructura de datos que nos permite almacenar pares de clave-valor. Son muy útiles para representar información que tiene una relación entre dos elementos.
#Se definen utilizando llaves {} y los elementos se separan por comas. Cada elemento se compone de una clave y un valor, separados por dos puntos :.
#sintaxis: diccionario = {clave1: valor1, clave2: valor2, clave3: valor3, ...}, las claves deben ser únicas y los valores pueden ser de cualquier tipo de dato.
#se puede acceder a los valores del diccionario utilizando la clave correspondiente, por ejemplo: diccionario[clave1] devuelve el valor asociado a la clave1.

midiccionario={"Alemania":"Berlín", "Francia":"París", "España":"Madrid", "Italia":"Roma"}

midiccionario["China"]="Shanghái" #agregamos un nuevo elemento al diccionario, si la clave ya existe, se actualiza el valor asociado a esa clave

midiccionario["China"]="Pekín" #corregimos el valor asociado a la clave "China"

print(midiccionario["Francia"])

print(midiccionario.get("España")) #otra forma de acceder a los valores del diccionario, utilizando el método get(), devuelve None si la clave no existe

del midiccionario["Italia"] #eliminamos un elemento del diccionario utilizando la palabra reservada del, si la clave no existe, se genera un error

midiccionario.pop("Alemania") #eliminamos un elemento del diccionario utilizando el método pop(), si la clave no existe, se genera un error

midiccionario2={23:"Jordan", "mosqueteros":3, "pi":3.1416} #los diccionarios pueden tener claves de diferentes tipos de datos, pero es recomendable utilizar siempre el mismo tipo de dato para las claves

mitupla=["España", "Francia", "Italia"]
midiccionario3={mitupla[0]:"Madrid", mitupla[1]:"París", mitupla[2]:"Roma"} #también se pueden utilizar listas como claves del diccionario, pero es recomendable utilizar tuplas, 
#ya que las listas son mutables y pueden generar errores

print(midiccionario3["Francia"]) 

#se pueden crear diccionarios dentro de diccionarios, es decir, un diccionario puede contener otro diccionario como valor asociado a una clave.
midiccionario4={"España":{"capital":"Madrid", "moneda":"Euro"}, "Francia":{"capital":"París", "moneda":"Euro"}, "Italia":{"capital":"Roma", "moneda":"Euro"}}
print(midiccionario4.keys()) #obtenemos las claves del diccionario, devuelve un objeto de tipo dict_keys, que se puede convertir en una lista utilizando la función list()
print(midiccionario4.values()) #obtenemos los valores del diccionario, devuelve un objeto de tipo dict_values, que se puede convertir en una lista utilizando la función list()
print(len(midiccionario4)) #obtenemos la longitud del diccionario, es decir, el número de elementos que contiene










