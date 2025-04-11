# 0 [[1 2 3],
# 1 [4 5 6],
# 2 [7 8 9]]

# para acceder al numero 9 nos movemos en filas y columnas
# fila 2, columna 2  -->  var = [2,2]  --> var = 9

matrix = [[1,2,3],
          [4,6,6],
          [7,8,9]]

print(matrix)

#para acceder a un elemento de la matris es mediante su posicion
print(matrix[0]) 

#añadimos una dimension mas  

#esto es una lista de listas
# 0 [[[1 2],[3 4]],
# 1 [[5 6][7 8]]]

# [1] [0] [1] ---> en esta posicion esta el elemento 6

#las matrices tienen las mismas propiedades de las listas

#tuplas: se caracteriza porque se escribe con parentesis y 
#sus elementos separados entre parentesis

numbers = (1,2,3,4,5)
print(numbers)
print(type(numbers))

#accedemos a un elemento
print(numbers[0]) 

#reescribimos una posicion
numbers[1] = "unCulo"
print(numbers)

#genera error porque las tuplas son inmutables
#o sea, no se pueden modificar