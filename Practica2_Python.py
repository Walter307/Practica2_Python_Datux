# PRACTICA NRO 2
#  DEFINA EL SIGUIENTE DICCIONARIO
ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]

# 1. CREA UN MENU ITERATIVO QUE CUENTE CON LAS SIGUIENTES OPCIONES:
# 2. Mostrar el listado de ventas => puedes usar print(f"")
# 3. Añadir un producto
# 4. Calcular la suma total de las ventas
# 5. Calcular el promedio de ventas
# 6. Mostar el producto que tiene más unidades vendidas
# 7. Mostrar el listado de productos


### SOLUCIÓN:


def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Mostrar el listado de ventas")
    print("2. Añadir un producto")
    print("3. Calcular la suma total de las ventas")
    print("4. Calcular el promedio de ventas")
    print("5. Mostrar el producto con más unidades vendidas")
    print("6. Mostrar el listado de productos")
    print("7. Salir")

from datetime import datetime   #Validación de fechas

def mostrar_ventas():
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {venta['promocion']}")

def validar_fecha():
    while True:
        fecha = input("Ingrese la fecha (dd-mm-aaaa): ")
        try:
            datetime.strptime(fecha, "%d-%m-%Y")
            return fecha
        except ValueError:
            print("Fecha inválida. Debe tener el formato dd-mm-aaaa.")

def añadir_producto():
    fecha = validar_fecha()
    while True:
        producto = input("Ingrese el nombre del producto: ").strip()
        if producto == "":
            print("El nombre del producto no puede estar vacío.")
        else:
            break
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad vendida: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Ingrese un número válido para la cantidad.")
    while True:
        try:
            precio = float(input("Ingrese el precio unitario: "))
            if precio <= 0:
                print("El precio debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Ingrese un número válido para el precio.")
    promocion = input("¿Está en promoción? (si/no): ").strip().lower() == 'si'
    nueva_venta = {"fecha": fecha, "producto": producto, "cantidad": cantidad, "precio": precio, "promocion": promocion}
    ventas.append(nueva_venta)
    print("Producto añadido exitosamente.")

def calcular_total_ventas():
    total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    print(f"El total de todas las ventas es: {total:.2f}")

def calcular_promedio_ventas():
    total_ventas = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    promedio = total_ventas / len(ventas) if ventas else 0
    print(f"El promedio de ventas es: {promedio:.2f}")

def producto_mas_vendido():
    productos = {}
    for venta in ventas:
        productos[venta['producto']] = productos.get(venta['producto'], 0) + venta['cantidad']
    max_cantidad = max(productos.values())
    productos_maximos = [producto for producto, cantidad in productos.items() if cantidad == max_cantidad]
    print("Producto(s) con más unidades vendidas:")
    for producto in productos_maximos:
        print(f"- {producto} con {max_cantidad} unidades")

def mostrar_productos():
    productos_unicos = set(venta['producto'] for venta in ventas)
    print("Listado de productos:")
    for producto in productos_unicos:
        print(f"- {producto}")

def menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            mostrar_ventas()
        elif opcion == '2':
            añadir_producto()
        elif opcion == '3':
            calcular_total_ventas()
        elif opcion == '4':
            calcular_promedio_ventas()
        elif opcion == '5':
            producto_mas_vendido()
        elif opcion == '6':
            mostrar_productos()
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Llamar al menú principal
menu()




