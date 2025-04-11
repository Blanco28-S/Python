#diccionario llamado nombre

numbers = {1:"uno",2:"dos", 3:"tres"}
print(numbers)

#para acceder a la informacion debemos acceder mediante las llaves

print(numbers[2])

#otro diccionario

information = {"nombre":"naiceyni",
               "apellido:":"blanco",
               "altura":1.60,
               "edad": 25}

del information["edad"]
print(information)
print(information["nombre"])
print(information["altura"])

#metodos propios de los diccionarios

# para saber cuales son las claves o llaves

claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)

#para extraer los pares de valor

pairs = information.items()
print(pairs)

#agenda de contacto utilizando un diccionario de diccionarios

contacts = {"naiceyni": {"Apellido:":"blanco",
               "Altura":1.60,
               "Edad": 25}, 
            "antonio": {"Apellido:":"perez",
               "Altura":1.96,
               "Edad": 89}
            }

print(contacts["naiceyni"])
print(contacts["antonio"])
