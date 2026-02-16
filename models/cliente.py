class Cliente:
    """
    Clase base Cliente.
    Define los atributos comunes para cualquier tipo de cliente.
    """

    def __init__(self, nombre: str, email: str, telefono: str, direccion: str):
        self.nombre = nombre.strip()
        self.email = email.strip().lower()
        self.telefono = telefono.strip()
        self.direccion = direccion.strip()

    def tipo_cliente(self) -> str:
        """Retorna el tipo del cliente (se sobreescribe en las subclases)."""
        return "Base"


class ClienteRegular(Cliente):
    """Cliente normal (sin beneficios especiales)."""

    def tipo_cliente(self) -> str:
        return "Regular"


class ClientePremium(Cliente):
    """Cliente con beneficios premium."""

    def tipo_cliente(self) -> str:
        return "Premium"


class ClienteCorporativo(Cliente):
    """Cliente empresa/corporativo."""

    def tipo_cliente(self) -> str:
        return "Corporativo"