# Funció per sumar els números entre dos números donats
def sumar_numeros(inici, fi):
    suma = 0
    for i in range(inici, fi + 1):
        suma += i
    return suma

# Sol·licitar a l'usuari que introdueixi dos números
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

# Calcular la suma
resultado = sumar_numeros(min(num1, num2), max(num1, num2))

# Mostrar el resultat
print(f"La suma dels números entre {num1} i {num2} (incloent-hi) és: {resultado}")