#hallar los numero scuadrados de los numeros del1 al 10

squares = [x**2 for x in range(1,11)]
print("Cuadrados:", squares)

#calculo de grados celsius a grados

celsius = [0,10,20,30,40]
fahrenheit = [(temp * 9/5) *32 for temp in celsius]
print("temperatura en grados F:", fahrenheit)

#numeros pares

evens = [x for x in range(1,21) if x%2 == 0]
print(evens)

#numeros impares

evens = [x for x in range(1,21) if x%2 != 0]
print(evens)

#traspuesta de una matriz

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
#print(transposed)

#mostrar en varias lineas de codigo

transposed = []
for i in range(len(matrix[0])):  #CREA LAS FILAS DE LA TRANPUESTA
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)
        
print(transposed)


#hecho por la profesora

squares = [x**2 for x in range(1,11)]
#print("Cuadrados:", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) *32 for temp in celsius]
#print("Temperatura en F:", fahrenheit)

#Numeros pares
evens = [x for x in range(1,21) if x%2 ==0]
#print(evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
#print(transposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)