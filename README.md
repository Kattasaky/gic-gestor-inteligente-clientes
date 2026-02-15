# Gestor Inteligente de Clientes (GIC)

Proyecto desarrollado en Python como parte del Módulo #4 del bootcamp.

El objetivo del sistema es implementar una solución escalable para la gestión de clientes, aplicando Programación Orientada a Objetos (POO), validaciones avanzadas, persistencia con SQLite, exportación de datos y buenas prácticas como logging y pruebas unitarias.


## Descripción del problema

La empresa ficticia SolutionTech necesita modernizar su sistema de gestión de clientes. Actualmente, los datos se administran manualmente, lo que provoca duplicación de registros, errores frecuentes, baja trazabilidad y dificultades para escalar.


## Objetivo del sistema

El sistema permite:

- Crear, editar y eliminar clientes
- Diferenciar tipos de clientes: Regular, Premium y Corporativo
- Validar email, teléfono y dirección
- Guardar datos en SQLite
- Exportar e importar clientes en JSON y CSV
- Registrar actividad del sistema mediante logs
- Integrarse con una API externa (validación simulada)
- Incluir pruebas unitarias básicas


## Tecnologías utilizadas

- Python 3
- SQLite (sqlite3)
- JSON / CSV (módulos estándar)
- Requests (integración con API)
- Logging
- Unittest


## Estructura del proyecto

gic-gestor-inteligente-clientes/
app/
main.py
models/
services/
utils/
data/
docs/
tests/
README.md
requirements.txt


---

## Instalación y ejecución

1. Clonar el repositorio:

bash
git clone https://github.com/Kattasaky/gic-gestor-inteligente-clientes.git
cd gic-gestor-inteligente-clientes
# Instalación de dependencias
pip install -r requirements.txt
# Ejecución de aplicación
python -m app.main
# Ejecución de pruebas
python -m unittest discover -s tests

UML

El modelo UML se encuentra en la carpeta:
docs/

Notas

La interfaz de esta entrega se implementa mediante consola (CLI). Una interfaz gráfica en Tkinter se considera como mejora futura.

Autor

Proyecto desarrollado por Katherine Vergara.2026

