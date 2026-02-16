import sqlite3
import os
from typing import List, Dict, Optional


class SQLiteRepoClientes:
    """
    Repositorio SQLite (persistencia).

    Se encarga de:
    - crear la base y la tabla si no existen
    - ejecutar CRUD
    """

    def __init__(self, db_path: str = "data/clientes.db"):
        self.db_path = db_path
        self._asegurar_directorio()
        self._crear_tabla()

    def _asegurar_directorio(self):
        os.makedirs("data", exist_ok=True)

    def _conectar(self):
        return sqlite3.connect(self.db_path)

    def _crear_tabla(self):
        query = """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            telefono TEXT NOT NULL,
            direccion TEXT NOT NULL,
            tipo TEXT NOT NULL
        );
        """
        with self._conectar() as conn:
            conn.execute(query)
            conn.commit()

    def crear(self, cliente_dict: Dict) -> None:
        query = """
        INSERT INTO clientes (nombre, email, telefono, direccion, tipo)
        VALUES (?, ?, ?, ?, ?);
        """
        with self._conectar() as conn:
            conn.execute(query, (
                cliente_dict["nombre"],
                cliente_dict["email"],
                cliente_dict["telefono"],
                cliente_dict["direccion"],
                cliente_dict["tipo"]
            ))
            conn.commit()

    def listar(self) -> List[Dict]:
        query = """
        SELECT nombre, email, telefono, direccion, tipo
        FROM clientes
        ORDER BY nombre ASC;
        """
        with self._conectar() as conn:
            cursor = conn.execute(query)
            filas = cursor.fetchall()

        clientes = []
        for fila in filas:
            clientes.append({
                "nombre": fila[0],
                "email": fila[1],
                "telefono": fila[2],
                "direccion": fila[3],
                "tipo": fila[4]
            })

        return clientes

    def obtener_por_email(self, email: str) -> Optional[Dict]:
        query = """
        SELECT nombre, email, telefono, direccion, tipo
        FROM clientes
        WHERE email = ?;
        """
        with self._conectar() as conn:
            cursor = conn.execute(query, (email,))
            fila = cursor.fetchone()

        if not fila:
            return None

        return {
            "nombre": fila[0],
            "email": fila[1],
            "telefono": fila[2],
            "direccion": fila[3],
            "tipo": fila[4]
        }

    def eliminar_por_email(self, email: str) -> bool:
        query = "DELETE FROM clientes WHERE email = ?;"
        with self._conectar() as conn:
            cursor = conn.execute(query, (email,))
            conn.commit()

        return cursor.rowcount > 0

    def actualizar_por_email(self, email: str, nuevos_datos: Dict) -> bool:
        query = """
        UPDATE clientes
        SET nombre = ?, telefono = ?, direccion = ?, tipo = ?
        WHERE email = ?;
        """
        with self._conectar() as conn:
            cursor = conn.execute(query, (
                nuevos_datos["nombre"],
                nuevos_datos["telefono"],
                nuevos_datos["direccion"],
                nuevos_datos["tipo"],
                email
            ))
            conn.commit()

        return cursor.rowcount > 0