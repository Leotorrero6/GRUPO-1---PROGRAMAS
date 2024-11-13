numeros = {1:"uno", 2:"dos", 3:"tres"}
print(numeros[2])
info = {"nombre": "Dayana",
               "Apellido": "Rodriguez",
               "Altura": 1.53,
               "Edad": 21}
print(info)
del info["Edad"]
print(info)
claves = info.keys()
print(claves)
print(type(claves))
values = info.values()
print(values)
pares = info.items()
print(pares)
contacto = {"Dayana":{ "Apellido": "Rodriguez","Altura": 1.53,"Edad": 21},
              "Eric": {"Apellido": "Zamora", "Altura": 1.70,"Edad": 22}}
print(contacto["Eric"])