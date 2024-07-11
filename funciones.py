class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    MAX_PRODUCTOS = 100

    def __init__(self):
        self.productos = []

    def ingresar_producto(self):
        if len(self.productos) >= Inventario.MAX_PRODUCTOS:
            print("El inventario está lleno.")
            return

        nombre = input("Ingresar nombre del producto: ")
        cantidad = int(input("Ingresar cantidad del producto: "))
        precio = float(input("Ingresar precio del producto: "))

        producto = Producto(nombre, cantidad, precio)
        self.productos.append(producto)
        print("Producto ingresado correctamente.")

    def listar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return

        print("Lista de productos:")
        for i, producto in enumerate(self.productos, start=1):
            print(f"Producto {i}:")
            print(f"  Nombre: {producto.nombre}")
            print(f"  Cantidad: {producto.cantidad}")
            print(f"  Precio: {producto.precio:.2f}")

    def editar_producto(self):
        index = int(input(f"Ingrese el índice del producto a editar (1-{len(self.productos)}): ")) - 1

        if index < 0 or index >= len(self.productos):
            print("Índice inválido.")
            return

        producto = self.productos[index]

        nombre = input(f"Editar nombre del producto (actual: {producto.nombre}): ")
        cantidad = int(input(f"Editar cantidad del producto (actual: {producto.cantidad}): "))
        precio = float(input(f"Editar precio del producto (actual: {producto.precio:.2f}): "))

        producto.nombre = nombre
        producto.cantidad = cantidad
        producto.precio = precio

        print("Producto editado correctamente.")

    def eliminar_producto(self):
        index = int(input(f"Ingrese el índice del producto a eliminar (1-{len(self.productos)}): ")) - 1

        if index < 0 or index >= len(self.productos):
            print("Índice inválido.")
            return

        self.productos.pop(index)
        print("Producto eliminado correctamente.")

def main():
    inventario = Inventario()
    opcion = 0
    while opcion != 5:
        print("\n***** Sistema de Inventarios *****")
        print("***** 1. Ingresar producto    *****")
        print("***** 2. Listar productos     *****")
        print("***** 3. Editar producto      *****")
        print("***** 4. Eliminar producto    *****")
        print("***** 5. Salir                *****")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            inventario.ingresar_producto()
        elif opcion == 2:
            inventario.listar_productos()
        elif opcion == 3:
            inventario.editar_producto()
        elif opcion == 4:
            inventario.eliminar_producto()
        elif opcion == 5:
            print("Saliendo del sistema.")
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
