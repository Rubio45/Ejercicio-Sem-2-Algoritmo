"""2. Escribir un programa que permita emitir la FACTURA correspondiente, a una compra de un artículo determinado,
del que se adquieren una o varias unidades.
El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad), es mayor de 1000, 
se aplicará un descuento del 12%."""

def calcular_factura(precio, cantidad):
    iva = 0.15
    descuento = 0.12
    subtotal = precio * cantidad
    descuento_bool = False
    total = subtotal * (1 + iva)
    if subtotal > 1000:
        total = total * (1 - descuento)
        descuento_bool = True
    return subtotal, total, descuento_bool

def hacer_factura(precio, cantidad):
    subtotal, total, descuento_bool = calcular_factura(precio, cantidad)
    print(f"Precio: {precio} C$ por unidad")
    print(f"Cantidad: {cantidad} unidades")
    print(f"Subtotal: {subtotal} C$")
    print(f"Total: {total} C$")
    if descuento_bool:
        print("Se aplicó un descuento del 12%.")
    else:
        print("No se aplicó descuento.")
    

if __name__ == "__main__":
    flag = 1
    while flag != 0:
        precio = float(input("Introduzca el precio del artículo: "))
        cantidad = int(input("Introduzca la cantidad de artículos: "))
        hacer_factura(precio, cantidad)
        flag = int(input("Desea continuar? (0 para salir): "))
    