"""
Se desea escribir un programa para el cálculo del área de diversas superficies:
cuadrado, rectángulo, círculo, triángulo y trapecio. El programa mostrará al inicio el siguiente menú:
Seguidamente leerá de la entrada estándar un valor que estará comprendido entre 1 y 5, 
indicando el tipo de superficie cuya área se desea calcular.  
El programa leerá entonces los datos que necesite para calcular el área en cuestión.  
El resultado se mostrará en la salida estándar, tras lo cual el programa terminará.
"""

import math

def mostrar_menu():
    print("¿Qué superficie desea calcular?")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")
    print("4. Triángulo")
    print("5. Trapecio")
    print("0. Salir")
    
def calcular_area_cuadrado(lado: float) -> float:
    return lado ** 2

def calcular_area_rectangulo(base: float, altura: float) -> float:
    return base * altura

def calcular_area_circulo(radio: float) -> float:
    return math.pi * radio ** 2

def calcular_area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

def calcular_area_trapecio(base_mayor: float, base_menor: float, altura: float) -> float:
    return ((base_mayor + base_menor) * altura) / 2

def main():
    mostrar_menu()
    opcion = int(input("Su opción: "))
    while opcion != 0:
        match opcion:
            case 1:
                lado = float(input("Ingrese el lado del cuadrado: "))
                print(f"El área del cuadrado es: {calcular_area_cuadrado(lado)}")
            case 2:
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                print(f"El área del rectángulo es: {calcular_area_rectangulo(base, altura)}")
            case 3:
                radio = float(input("Ingrese el radio del círculo: "))
                print(f"El área del círculo es: {calcular_area_circulo(radio)}")
            case 4:
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                print(f"El área del triángulo es: {calcular_area_triangulo(base, altura)}")
            case 5:
                base_mayor = float(input("Ingrese la base mayor del trapecio: "))
                base_menor = float(input("Ingrese la base menor del trapecio: "))
                altura = float(input("Ingrese la altura del trapecio: "))
                print(f"El área del trapecio es: {calcular_area_trapecio(base_mayor, base_menor, altura)}")
            case _:
                print("Opción invalida.")
        mostrar_menu()
        opcion = int(input("Su opción: "))
        
if __name__ == "__main__":
    main()
