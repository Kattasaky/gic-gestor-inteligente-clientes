from services.gestor_clientes import GestorClientes


def main():
    gestor = GestorClientes()

    # 1) Crear cliente
    gestor.crear_cliente(
        tipo="Premium",
        nombre="Katta",
        email="katta@gmail.com",
        telefono="+56912345678",
        direccion="Av. Siempre Viva 123"
    )

    # 2) Listar
    print("\nLISTA CLIENTES:")
    for c in gestor.listar_clientes():
        print(c)

    # 3) Editar
    gestor.editar_cliente(
        email="katta@gmail.com",
        tipo="Corporativo",
        nombre="Katta Actualizada",
        telefono="+56987654321",
        direccion="Nueva Dirección 999"
    )

    print("\nLISTA CLIENTES (ACTUALIZADA):")
    for c in gestor.listar_clientes():
        print(c)

    # 4) Eliminar
    gestor.eliminar_cliente("katta@gmail.com")

    print("\nLISTA CLIENTES (DESPUÉS DE ELIMINAR):")
    for c in gestor.listar_clientes():
        print(c)


if __name__ == "__main__":
    main()