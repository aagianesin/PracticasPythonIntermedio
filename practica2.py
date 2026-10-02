# Ejercicio 1
try:
    num1 = float(input("Ingrese el primer número (numerador): "))
    num2 = float(input("Ingrese el segundo número (denominador): "))
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir un número por cero.")

# Ejercicio 2
try:
    numero = float(input("Ingrese un número: "))
    cadena = input("Ingrese una cadena de texto: ")
    resultado = numero + cadena
    print(resultado)
except TypeError:
    print("no se puede sumar un número y una cadena")

# Ejercicio 3
try:
    datos = {"nombre": "Peter", "edad": 15}
    print(datos["apellido"])
except KeyError:
    print("Error: La clave a la que intentas acceder no existe en el diccionario.")

# Ejercicio 4
nombre_archivo = "parker.txt"
try:
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe. Creándolo ahora...")
    with open(nombre_archivo, "w") as archivo:
        archivo.write("Este es un archivo creado automáticamente por el programa.")
    print("¡Archivo creado exitosamente!")

# Ejercicio 5
try:
    numerador = int(input("Ingrese el primer número (entero): "))
    denominador = int(input("Ingrese el segundo número (entero): "))
    
    resultado = numerador / denominador
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: El segundo número no puede ser cero (división por cero).")
except ValueError:
    print("Error: Has ingresado un valor no válido (se esperaba un número entero).")
