import logging
import os


def configurar_logger(nombre: str = "gic_logger") -> logging.Logger:
    """
    Crea y retorna un logger configurado.
    Escribe logs en consola y en logs/app.log
    """
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    # Evita duplicar handlers si se llama varias veces
    if logger.handlers:
        return logger

    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # Handler archivo
    file_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
    file_handler.setFormatter(formato)

    # Handler consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formato)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger