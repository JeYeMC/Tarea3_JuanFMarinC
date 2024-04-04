import csv


class LectorCSV:
    @staticmethod
    def leer_datos_csv(archivo_csv):
        """
        Lee los datos del archivo CSV y devuelve una lista de diccionarios.
        """
        datos = []
        with open(archivo_csv, 'r') as archivo:
            lector_csv = csv.reader(archivo)
            # next(lector_csv)  # Saltar la primera fila si contiene encabezados
            for fila in lector_csv:
                estudiante = {
                    'id': fila[0],
                    'nombre': fila[1],
                    'apellido': fila[2]
                }
                datos.append(estudiante)
        return datos
