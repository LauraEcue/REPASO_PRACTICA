#FUNCIONES DE UN VECTOR
#append() agrega valor
numeros = [10, 20, 30]
numeros.append(40)
print(numeros)


#insert() insertar por posición
numeros = [10, 20, 30]
numeros.insert(1, 15)
print(numeros)


#remove() elimina por valor
numeros = [10, 20, 30]
numeros.remove(20)
print(numeros)


#pop() elimina por indice
numeros = [10, 20, 30]
numeros.pop(1)
print(numeros)


#len() conoce el tamaño
numeros = [10, 20, 30]
print(len(numeros))


#index() buscar posición
numeros = [10, 20, 30]
print(numeros.index(20))


#count( contar repeticiones)
numeros = [10, 20, 30, 20, 10]
print(numeros.count(30))


#sort() ordenar
numeros = [40, 30, 10, 20]
numeros.sort()
print(numeros)


#reverse() invertir
numeros = [10,30,20,5]
numeros.reverse()
print(numeros)


#clear() vaciar

numeros = [10,20,30,50]
numeros.clear()
print(numeros)



#RECORRER UN VECTOR
numeros = [10,20,30,40]
for i in range(len(numeros)):  #PRIMERA FORMA
    print(numeros[i])

for numero in numeros:         #SEGUNDA FORMA
    print(numero)



