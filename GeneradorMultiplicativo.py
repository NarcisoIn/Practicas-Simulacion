def multiplicativo(semilla, a, m, cantidad):
    """
    Generador de números pseudoaleatorios multiplicativo
    semilla: número inicial (X0, no 0)
    a: multiplicador
    m: módulo
    cantidad: cantidad de números a generar
    """
    if semilla == 0:
        print("La semilla no puede ser 0 para el generador multiplicativo.")  # noqa: E501
        return

    numeros = []
    X = semilla
    for i in range(cantidad):
        X = (a * X) % m
        numeros.append(X)
        print(f"X{i+1}: {X}")
    print("Secuencia generada:", numeros)


# Lo que hace el codigo
print("Programa de generación de numeros Pseudoaleatorios")
print("por el Método de Generación Congruencial Multiplicativo")

# Ejemplo de uso
cantidad = int(input("Cantidad de números a generar: "))
semilla = int(input("Ingresa la semilla (X0, > 0): "))
a = int(input("Ingresa el multiplicador (a): "))
m = int(input("Ingresa el módulo (m): "))

secuencia = multiplicativo(semilla, a, m, cantidad)
