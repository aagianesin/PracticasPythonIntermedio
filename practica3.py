# Ejercicio 1

numero1 = float(input())

numero2 = float(input())

mayor = numero1 if numero1 > numero2 else numero2

print(mayor)


# Ejercicio 2

def buscar_palabra(palabra_buscada, *palabras):
    return f"Palabra {palabra_buscada} encontrada" if palabra_buscada in palabras else "Palabra no encontrada"

print(buscar_palabra("DragonBall", "Ben10", "Spiderman", "DragonBall", "PowerRangers"))


# Ejercicio 3

numero = int(input())

ternario = "par" if numero % 2 == 0 else "impar"

print(f"El número es {ternario}")


# Ejercicio 4

def calcular_promedio(*numeros):
    return sum(numeros) / len(numeros) if len(numeros) > 0 else 0

print(calcular_promedio(10, 5, 9, 7))


# Ejercicio 5
def verificar_cantidad_argumentos(*args):
    return "Error" if len(args) < 2 else args

print(verificar_cantidad_argumentos("programa"))
