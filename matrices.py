#ACCEDER A UN ELEMENTO - FUNCIONES
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0][0])
print(matriz[1][2])
print(len(matriz))          #numeros de filas

print(len(matriz[0]))       #numero de columnas

# print(matriz[][])  acceder a un elemento

matriz[0][0]= 10            #modificar elemento
print (matriz)  

matriz.append([10, 11,12])  #agregar fila
print (matriz)

matriz.pop(0)               #eliminar una fila
print(matriz)

matriz[0].append(4)         #agregar elemento a una fila
print(matriz)

matriz[0].pop(3)            #eliminar elemento
print(matriz)


#RECORRER UNA MATRIZ
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in range(len(matriz)):     #normal izquierda a derecha
    for columna in range(len(matriz[fila])):
        print(matriz[fila][columna])

for fila in range(len(matriz)):     #izquierda a derecha
    for columna in range(len(matriz[fila])):
        print(matriz[fila][columna], end=" ")
    print()

for fila in range(len(matriz)):    #derecha a izquierda
    for columna in range(len(matriz[fila])-1, -1, -1):
        print(matriz[fila][columna], end=" ")
    print()

for columna in range(len(matriz[0])):   #arriba hacia abajo
    for fila in range(len(matriz)):
        print(matriz[fila][columna], end=" ")
    print()

for columna in range(len(matriz[0])):   #abajo hacia arriba
    for fila in range(len(matriz)-1, -1, -1):
        print(matriz[fila][columna], end=" ")
    print()

for fila in range(len(matriz)-1, -1, -1):   #abajo hacia arriba y de derecha a izquierda
    for columna in range(len(matriz[fila])-1, -1, -1):
        print(matriz[fila][columna], end=" ")
    print()

# Recorrido normal
#range(len(matriz))

# Recorrido inverso
#range(len(matriz)-1, -1, -1)

# Recorrido normal de columnas
#range(len(matriz[0]))

# Recorrido inverso de columnas
#range(len(matriz[0])-1, -1, -1)

