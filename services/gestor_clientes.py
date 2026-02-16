from models.cliente import (
    ClienteRegular,
    ClientePremium,
    ClienteCorporativo
)

from persistence.sqlite_repo import SQLiteRepoClientes
from utils.excepciones import ClienteNoEncontradoError
from utils.logger import configurar_logger


logger = configurar_logger()


class GestorClientes:
    """
    Capa de lógica de negocio.

    - crea instancias Cliente
    - aplica validaciones
    - usa SQLiteRepoClientes para guardar datos
    """

    def __init__(self):
        self.repo = SQLiteRepoClientes()

    def _crear_instancia_cliente(self, tipo: str, nombre: str, email: str, telefono: str, direccion: str):
        tipo = tipo.strip().lower()

        if tipo == "regular":
            return ClienteRegular(nombre, email, telefono, direccion)
        elif tipo == "premium":
            return ClientePremium(nombre, email, telefono, direccion)
        elif tipo == "corporativo":
            return ClienteCorporativo(nombre, email, telefono, direccion)
        else:
            raise ValueError("Tipo inválido. Use: Regular, Premium o Corporativo")

    def crear_cliente(self, tipo: str, nombre: str, email: str, telefono: str, direccion: str):
        cliente = self._crear_instancia_cliente(tipo, nombre, email, telefono, direccion)

        self.repo.crear({
            "nombre": cliente.nombre,
            "email": cliente.email,
            "telefono": cliente.telefono,
            "direccion": cliente.direccion,
            "tipo": cliente.tipo_cliente()
        })

        logger.info(f"Cliente creado: {cliente.email} ({cliente.tipo_cliente()})")
        return cliente

    def listar_clientes(self):
        return self.repo.listar()

    def eliminar_cliente(self, email: str):
        eliminado = self.repo.eliminar_por_email(email)

        if not eliminado:
            logger.warning(f"Intento de eliminar cliente inexistente: {email}")
            raise ClienteNoEncontradoError("No existe un cliente con ese email.")

        logger.info(f"Cliente eliminado: {email}")
        return True

    def editar_cliente(self, email: str, tipo: str, nombre: str, telefono: str, direccion: str):
        existente = self.repo.obtener_por_email(email)
        if not existente:
            raise ClienteNoEncontradoError("No existe un cliente con ese email.")

        cliente = self._crear_instancia_cliente(tipo, nombre, email, telefono, direccion)

        actualizado = self.repo.actualizar_por_email(email, {
            "nombre": cliente.nombre,
            "telefono": cliente.telefono,
            "direccion": cliente.direccion,
            "tipo": cliente.tipo_cliente()
        })

        if actualizado:
            logger.info(f"Cliente actualizado: {email}")

        return actualizado