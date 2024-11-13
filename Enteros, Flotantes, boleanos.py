
edad = int(input("Por favor, introduce tu edad: "))
mayoria_edad = edad >= 20

if mayoria_edad:
    print(type(mayoria_edad))
    print("Acceso concedido. Puedes continuar usando el programa.")

    numero_entero = int(input("Introduce un número entero: "))
    print(f"El valor entero ingresado es: {numero_entero} (tipo: {type(numero_entero)})")

    numero_flotante = float(input("Introduce un número de punto flotante: "))
    print(f"El valor flotante ingresado es: {numero_flotante} (tipo: {type(numero_flotante)})")

    print("¡Gracias por usar el programa!")
else:
    print(type(mayoria_edad))
    print("Acceso denegado. Debes ser mayor de 20 años para usar este programa.")