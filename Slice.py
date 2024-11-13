# Empezamos Definiendo una lista de números
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Utilizamos el metodo slice para obtener una parte de la lista
# Aquí obtenemos los elementos desde el índice 2 hasta el 5 (no incluye el 5)
sublista = numeros[2:5]
print("Sublista de elementos del índice 2 al 4:", sublista)

# Aquí tomamos los primeros cinco elementos de la lista
primeros_cinco = numeros[:5]
print("Primeros cinco elementos de la lista:", primeros_cinco)

# Aquí tomamos los últimos tres elementos de la lista
ultimos_tres = numeros[-3:]
print("Últimos tres elementos de la lista:", ultimos_tres)

# Aquí tomamos todos los elementos con dos saltos
con_saltos = numeros[::2]
print("Elementos cada dos posiciones:", con_saltos)

# En este punto,trabajamos con una cadena de texto
texto = "Bienvenidos a la clase"

# Aquí tomamos los caracteres del índice 0 al 4 
subcadena = texto[0:11]
print("Subcadena de los primeros cuatro caracteres:", subcadena)

# Usando slice para invertir la cadena
texto_invertido = texto[::-1]
print("Texto invertido:", texto_invertido)








