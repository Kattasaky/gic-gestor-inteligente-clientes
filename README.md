# Gestor Inteligente de Clientes (GIC)

Proyecto desarrollado en Python como parte del Módulo #4 del bootcamp.

El objetivo del sistema es implementar una solución organizada y escalable para la gestión de clientes, aplicando Programación Orientada a Objetos (POO), validaciones, persistencia con SQLite, exportación de datos y buenas prácticas como logging.

---

## Descripción del problema

La empresa ficticia SolutionTech necesita modernizar su sistema de gestión de clientes. Actualmente, los datos se administran manualmente, lo que provoca:

- Duplicación de registros
- Errores frecuentes en la información
- Baja trazabilidad de cambios
- Dificultades para escalar el sistema

---

## Objetivo del sistema

Este sistema permite gestionar clientes mediante una interfaz por consola (CLI), incluyendo:

- Crear clientes
- Listar clientes
- Buscar clientes
- Editar clientes
- Eliminar clientes
- Guardar los datos en SQLite
- Exportar datos (JSON y/o CSV según opción del menú)
- Registrar acciones del sistema mediante logs

---

## Tecnologías utilizadas

- Python 3
- SQLite (sqlite3)
- JSON / CSV (módulos estándar)
- Logging

---

## Estructura del proyecto

gic-gestor-inteligente-clientes/
│
├── app/
│ └── main.py
│
├── models/
│ └── cliente.py
│
├── services/
│ ├── gestor_clientes.py
│ └── validaciones.py
│
├── persistence/
│ └── sqlite_repo.py
│
├── utils/
│ ├── excepciones.py
│ └── logger.py
│
├── data/
│ ├── gic.db
│ └── export/
│
├── logs/
│ └── gic.log
│
├── docs/
│ └── uml.png
│
├── README.md
├── requirements.txt
└── .gitignore


---

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/Kattasaky/gic-gestor-inteligente-clientes.git
cd gic-gestor-inteligente-clientes

2. Instalar dependencias
pip install -r requirements.txt

3. Ejecutar la aplicación
python -m app.main

Persistencia (SQLite)

Los datos se guardan automáticamente en una base de datos SQLite ubicada en:

data/gic.db

Esto permite que la información se mantenga aunque se cierre el programa.

Logs del sistema

El sistema registra eventos importantes (creación, edición, eliminación, exportaciones, errores) en:

logs/gic.log

UML

El diagrama UML del sistema se encuentra en:

docs/uml.png

Notas

La interfaz de esta entrega se implementa mediante consola (CLI).
Una interfaz gráfica en Tkinter se considera como mejora futura.

Autor

Proyecto desarrollado por Katherine Vergara (2026).

