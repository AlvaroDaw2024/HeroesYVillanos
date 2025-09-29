'''En esta clase hacer toda la gestion del log'''
import logging
import os
from datetime import datetime


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._inicializado = False
        return cls._instance

    def __init__(self):
        if not self._inicializado:
            self._inicializado = True
            self.configurar_logging()

    def configurar_logging(self):

        if not os.path.exists('log'):
            os.makedirs('log')

        fecha = datetime.now().strftime("%d%m%Y")
        nombre_fichero = f"log/{fecha}_HEROESYVILLANOS.log"

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(nombre_fichero, encoding='utf-8'),

            ]
        )

        self.logger = logging.getLogger()


    def info(self, mensaje):

        self.logger.info(mensaje)

    def error(self, mensaje):

        self.logger.error(mensaje)

    def warning(self, mensaje):

        self.logger.warning(mensaje)

    def debug(self, mensaje):

        self.logger.debug(mensaje)

logger = Logger()