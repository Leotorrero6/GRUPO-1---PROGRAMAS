# Aqui mostramos el titulo del programa

print("Calculadora de Promedio Universidad")

# Para guardas las notas se crea una lista vacia en corchetes

notas = []
nota = input("Ingrese la nota (o presione Enter para terminar): ")

#para introduccir varios valores de manera indefinida se crea un ciclo while, 
# este ciclo pedira datos hasta que el usurio decidad terminarlo

while nota != "":
    notas.append(float(nota))
    nota = input("Ingrese otra nota (o presione Enter para terminar): ")

# Para hacer el proceso matematico del promedio se crea una variablle llamada promedio

promedio = sum(notas) / len(notas)

# y por ultimo Mostramos el resultado de la operacion de la variable promedio

print(F"Tu promedio es: {promedio:.2f}")
