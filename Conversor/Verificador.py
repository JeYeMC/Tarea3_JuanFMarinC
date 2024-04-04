import os


class VerificadorArchivo:
    @staticmethod
    def verificar_existencia_archivo(archivo_csv):
        """
        Verifica si el archivo CSV existe en la ruta especificada.
        """
        return os.path.exists(archivo_csv)
