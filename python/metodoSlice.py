a = [1,2,3,4]
b = a   
print(a)
print(a)

#modificacion

del a[0]
print(a)
print(a)

#hasta las lineas por encima de este comentario decimos que
# a y b son de la clase lista pero a su vez son como apuntadores
#porque al modificar la lista a se ve tambien el cambio en la 
#lista b

# para ver donde se almacena la informacion

print(id(a))
print(id(b))

#para no tener estos problemas de que las 
# acciones que se hagan en una varible se vean
# reflejadas en orta, se usa el slice

c = a[:]   #imprime todos los elementos desde la cero hasta el final

print(id(a))
print(id(b))
print(id(c))
a.append(6)
print(a)
print(b)
print(c)

