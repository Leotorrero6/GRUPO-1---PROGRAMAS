# Quehaceres del hogar
quehaceres = ["Lavar los trastes", 
              "Barrer y trapear el piso",
              "Hacer los alimentos", 
              "Poner la ropa a lavar"]
print(quehaceres)

# Lista con números y textos
numeros = [1, 2, 3, 4, "cinco"]
print(type(numeros))

# Mixta
mezcla = ["uno", 2, 3.14, True, [1, 2, 3]]
print(mezcla, len(mezcla), mezcla[0], mezcla[1], mezcla[-1], mezcla[2:-2])

# Operaciones con cadenas
texto = "Hola mundo"
print(texto[0], texto[1], texto[-1])

# Agregar elementos 
mezcla.append(False)
mezcla.append(["a", "b"])
mezcla.insert(1, ["a", "b"])
print(mezcla)

# Posición en la lista
print(mezcla.index(["a", "b"]))

# Lista de números
numeros_lista = [1, 2, 100.01, 90.45, 3, 4, 5]
print(numeros_lista, "Mayor:", max(numeros_lista), "Menor:", min(numeros_lista))

# Eliminar los elementos
del numeros_lista[-1]
del numeros_lista[:2]
print(numeros_lista)

# Eliminar completo
del numeros_lista
