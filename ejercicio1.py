def mostrar_menu():
    print("=" * 16)
    print("| HOLA USUARIO |")
    print("=" * 16)
    print("¿Qué vehículo usa?")
    print("1. Bicicleta")
    print("2. Moto")
    print("3. Carro")
    print("4. Camión")

def calcular_importe(vehiculo):
    if vehiculo == 1:
        precio_bicicleta = 100
        return precio_bicicleta
    elif vehiculo in [2, 3]: # esto es igual a vehiculo == 2 or vehiculo == 3
        precio_x_km_motos_carros = 30
        distancia = float(input("Introduzca la distancia que ha hecho en km: "))
        return precio_x_km_motos_carros * distancia
    elif vehiculo == 4:
        precio_x_km_camion = 30
        precio_x_tonelada_camion = 25
        distancia = float(input("Introduzca la distancia que ha hecho en km: "))
        peso = float(input("Introduzca el peso del vehículo en toneladas: "))
        return (precio_x_km_camion * distancia) + (precio_x_tonelada_camion * peso)
    else:
        print("Opción invalida.")
        return None

def main():
    flag = 0
    while flag != 0:
        mostrar_menu()
        try:
            vehiculo = int(input("Su vehículo: "))
            importe = calcular_importe(vehiculo)
            if importe is not None:
                print(f"El importe a pagar es: {importe} cordobas")
        except ValueError:
            print("Entrada no valida. Por favor, introduzca un numero.")
        flag = int(input("Desea continuar? (0 para salir): "))

if __name__ == "__main__":
    main()