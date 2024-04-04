import os


class CreadorArchivo:
    @staticmethod
    def crear_archivo_json(datos_json, archivo_csv):
        """
        Crea el archivo JSON si los datos están disponibles.
        """
        if datos_json:
            archivo_json = os.path.splitext(archivo_csv)[0] + '.json'
            with open(archivo_json, 'w') as archivo:
                archivo.write(datos_json)
            print(f"Se ha creado el archivo JSON: {archivo_json}")
