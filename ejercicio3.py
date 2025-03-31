"""3. Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, 
ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. 
Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso sobre 3. 
Diseñe un programa que determine el monto de la compra, el monto del descuento, el monto a pagar y 
el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto."""

def calcular_compra(docenas, precio):
    descuento_3_docenas = 0.15
    descuento_habitual = 0.10
    
    if docenas > 3:
        regalo = docenas - 3
        subtotal = precio * docenas * 12
        precio_total = subtotal * (1 - descuento_3_docenas)
        descuento = subtotal - precio_total
        unidades = (docenas * 12) + regalo
    else:
        subtotal = precio * docenas * 12
        precio_total = subtotal * (1 - descuento_habitual)
        descuento = subtotal - precio_total
        unidades = docenas * 12
    return subtotal, descuento, precio_total, unidades

def hacer_compra(docenas, precio):
    subtotal, descuento, precio_total, unidades = calcular_compra(docenas, precio)
    print(f"Docenas: {docenas}")
    print(f"Precio: {precio} C$ por unidad")
    print(f"Subtotal: {subtotal} C$")
    print(f"Descuento: {descuento} C$")
    print(f"Total: {precio_total} C$")
    print(f"Unidades en total: {unidades}")

if __name__ == "__main__":
    flag = 1
    while flag != 0:
        docenas = int(input("Introduzca la cantidad de docenas: "))
        precio = float(input("Introduzca el precio por unidad: "))
        hacer_compra(docenas, precio)
        flag = int(input("Desea continuar? (0 para salir): "))
        