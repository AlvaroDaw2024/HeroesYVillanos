import logging
import os

def configurar_logging():
    # Crear directorio log si no existe
    if not os.path.exists('log'):
        os.makedirs('log')
    
    fecha = datetime.now().strftime("%d%m%Y")
    nombre_fichero = f"log/{fecha}_HEROESYVILLANOS.log"
    
    logging.basicConfig(
        filename=nombre_fichero,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )