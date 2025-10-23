"""
Programa de generación de numeros Pseudoaleatorios por
el metodo de Generación Congruencial Lineal
"""
secuencia = []


# Funcion de Generacion Congruencial Lineal
def lgc(X0, a, c, m):
    global cantidad

    for i in range(1, cantidad+1):
        X = (a*X0 + c) % m
        X0 = X
        print(f"X{i}: {X}")
        secuencia.append(X)
    # Impresion de secuencia
    print(f"Secuencia: {secuencia}")


# Lo que hace el codigo
print("Programa de generación de numeros Pseudoaleatorios")
print("por el Método de Generación Congruencial Lineal")

# Entrada de datos por usuario
cantidad = int(input("¿Cuántos números quieres generar?: "))
X0 = int(input("Ingresa el valor de X_0: "))
a = int(input("Ingresa el valor de a: "))
c = int(input("Ingresa el valor de la constante c: "))
m = int(input("Ingresa el valor del modulo m: "))

# Llamada de funcion de generacion
lgc(X0, a, c, m)
