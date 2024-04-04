import json


class Convertidor:
    @staticmethod
    def convertir_a_json(datos):
        """
        Convierte los datos leídos del archivo CSV a formato JSON.
        """
        datos_json = json.dumps(datos, indent=4)
        return datos_json
