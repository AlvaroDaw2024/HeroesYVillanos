'''En esta clase hacer toda la gestion del log'''
from datetime import datetime
import logging as log


fecha = datetime.now().strftime("%d%m%Y").lower()
nombre_fichero = f"log/{fecha}_HEROESYVILLANOS.log"