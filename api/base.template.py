# Plantilla de configuración
# Copia esta seccion a 'base.py' y personalizalo
import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "dbname": "nombre_base_datos",
    "user": "usuario",
    "password": "contrasenia"
}

def conectar():
    return psycopg2.connect(**DB_CONFIG)
