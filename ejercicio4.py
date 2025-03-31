"""Diseñe un programa que lea un número de tres cifras y 
determine si es igual al revés del número."""

def check_number(number: int) -> bool:
    return str(number) == str(number)[::-1]

def check_number2(number: int) -> bool:
    number = str(number)
    return number[0] == number[-1]

def main():
    number = int(input("Ingrese un número de tres cifras: "))
    if number < 100 or number > 999:
        print("El número no es de tres cifras.")
        return
    if check_number(number):
        print(f"El número {number} se lee igual al revés.")
    else:
        print(f"El número {number} no se lee igual al revés.")

if __name__ == "__main__":
    flag = 1
    while flag != 0:
        main()
        flag = int(input("Desea continuar? (0 para salir): "))