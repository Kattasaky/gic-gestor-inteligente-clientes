import json
import csv
import os
from typing import List, Dict


def exportar_clientes_json(clientes: List[Dict], ruta: str = "data/clientes.json") -> str:
    os.makedirs("data", exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)

    return ruta


def exportar_clientes_csv(clientes: List[Dict], ruta: str = "data/clientes.csv") -> str:
    os.makedirs("data", exist_ok=True)

    campos = ["nombre", "email", "telefono", "direccion", "tipo"]

    with open(ruta, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for c in clientes:
            writer.writerow(c)

    return ruta