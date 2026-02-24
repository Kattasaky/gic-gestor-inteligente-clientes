from services.gestor_clientes import GestorClientes
from utils.excepciones import ClienteNoEncontradoError


def mostrar_menu():
    print("\n=== GESTOR INTELIGENTE DE CLIENTES ===")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente por email")
    print("4. Editar cliente")
    print("5. Eliminar cliente")
    print("0. Salir")


def main():
    gestor = GestorClientes()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                tipo = input("Tipo (Regular/Premium/Corporativo): ")
                nombre = input("Nombre: ")
                email = input("Email: ")
                telefono = input("Teléfono: ")
                direccion = input("Dirección: ")

                gestor.crear_cliente(tipo, nombre, email, telefono, direccion)
                print("Cliente creado correctamente.")

            elif opcion == "2":
                clientes = gestor.listar_clientes()
                if not clientes:
                    print("No hay clientes registrados.")
                else:
                    for c in clientes:
                        print(c)

            elif opcion == "3":
                email = input("Ingrese email: ")
                cliente = gestor.buscar_cliente(email)
                print(cliente)

            elif opcion == "4":
                email = input("Email del cliente a editar: ")
                tipo = input("Nuevo tipo (Regular/Premium/Corporativo): ")
                nombre = input("Nuevo nombre: ")
                telefono = input("Nuevo teléfono: ")
                direccion = input("Nueva dirección: ")

                gestor.editar_cliente(email, tipo, nombre, telefono, direccion)
                print("Cliente actualizado.")

            elif opcion == "5":
                email = input("Email del cliente a eliminar: ")
                gestor.eliminar_cliente(email)
                print("Cliente eliminado.")

            elif opcion == "0":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ClienteNoEncontradoError as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e)


if __name__ == "__main__":
    main()