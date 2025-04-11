to_do = ["Dirigirnos al Hotel", "Ir a Almozar",
         "Visitar un museo", "Volver al Hotel"]


print(to_do)

#una de las caracteristicas de las listas, es que tenemos
#libertad al momento de guardar informacion
#ejemplo:

numbers = [1,2,3,4,"cinco"]
print(numbers)

#ahora preguntaremos cual es el tipo de la informacion 
print(type (numbers))  # toma este tipo de datos como la class list 

mix = ["uno",2,3.14, True,[1,2,3]]

print(mix)

#tambien podemos consultar cuantos datos tenemos guardados

print("el numero de elementos de la clase mix es de: ", len(mix) )
#print(len(mix))

#tambien podemos indexar en la lista

print("Primer elemento:", mix[0], "que es de tipo: ", type(mix[0]))
print("segundo elemento:", mix[1], "que es de tipo: ", type(mix[1]))
print("tercer elemento:", mix[2], "que es de tipo: ", type(mix[2]))
print("ultimo elemento:", mix[-1], "que es de tipo: ", type(mix[-1]))

#tambien se indexa en las cadenas
#tambien podemos extraer porciones de nuestra informacion

string = "Hola Platzinauta"

#indexamos la cadena 

print(string)

print("Primer elemento:", string[0], "que es de tipo: ", type(string[0]))
print("segundo elemento:", string[1], "que es de tipo: ", type(string[1]))
print("tercer elemento:", string[2], "que es de tipo: ", type(string[2]))
print("ultimo elemento:", string[4], "que es de tipo: ", type(string[4]))
print("ultimo elemento:", string[9], "que es de tipo: ", type(string[9]))
print("ultimo elemento:", string[-1], "que es de tipo: ", type(string[-1]))

#laxin

print(mix[0:2])

#en caso de que quiera desde la posicion cero

print(mix[:2])

#en caso de que quiera desde la doa en adelante

print(mix[2:])

#nos devuelve el elemento qunico de la posicion

print(mix[2:-2])

#metodos de la clase listas:
#metodo append: agrega al final

print(mix)
mix.append(False)  
print(mix)
mix.append(["a", "b"])
print(mix)

#metodo insert: agrega en una posicion en especifico

mix.insert(0,"5")  
print(mix)

#metodo que muestra la primera aparicion del elemento

print(mix.index("5"))

#cuando se trabaja con listas de numeros 
#podemos consultar cual es el elemento mayor o el menor

#creamos una lista de numeros para el ejemplo 
numbers = [1,2,3,21,45,0,75,100,100.1]

#metdo max: que muestra el mayor de la lista 

print("Maximo:",max(numbers))

#metdo min: que muestra el menor de la lista 

print("Menor:",min(numbers))

#motodo del: para eliminar elementos de la lista

del numbers[-1]  #elimina el ultimo
print(numbers)

#eliminar una porcion de datos

del numbers[:2]
print(numbers)

#eliminar toda la lista

del numbers
print(numbers)