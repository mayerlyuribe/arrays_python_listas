#Magnitud o norma euclidiana de un vector
norma = 0 

n = int(input("Número de elementos del vector: ")) 
vector = [None] * n 
for i in range(n): 
    print("Posición:", i) 
    vector[i] = int(input("Valor: ")) 
for i in range(n): 
    norma = norma + vector[i]**2 
    norma = norma**0.5 
print("Vector generado:", vector) 
print("La magnitud del vector es:", norma) 
