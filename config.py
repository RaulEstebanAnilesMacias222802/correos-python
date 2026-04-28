# Configuración de base de datos SQLite
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

# Configuración de correo SMTP
SMTP_CONFIG = {
    'host': 'smtp.gmail.com',
    'port': 465,
    'sender_email': 'soporteuacjcast@gmail.com',
    'sender_password': 'bwtilydrroosimns',
    'sender_name': 'Soporte UACJ'
}

# Configuración de Flask
SECRET_KEY = 'tu_clave_secreta_aqui'
DEBUG = True
