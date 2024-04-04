from Lector import LectorCSV
from Convertidor import Convertidor
from Creador import CreadorArchivo
from Verificador import VerificadorArchivo


def principal():
    archivo_csv = input("Por favor, ingrese la ruta completa del archivo CSV: ")

    # Verificar si el archivo CSV existe
    if not VerificadorArchivo.verificar_existencia_archivo(archivo_csv):
        print("El archivo CSV especificado no existe.")
        return

    # Leer datos del archivo CSV
    datos = LectorCSV.leer_datos_csv(archivo_csv)

    # Convertir datos a formato JSON
    datos_json = Convertidor.convertir_a_json(datos)

    # Crear archivo JSON
    CreadorArchivo.crear_archivo_json(datos_json, archivo_csv)


if __name__ == "__main__":
    principal()
