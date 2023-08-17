#suma de los elementos de un vector
suma = 0
vector = [None]*5
for i in range(5):
    a = int(input("Dame un elemento: "))
    vector[i] = a
    suma += vector[i]
print("La suma de los elementos del vector es:", suma)