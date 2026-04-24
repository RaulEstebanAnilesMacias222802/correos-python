# Proyecto de Registro y Envío de Correos - Versión Python

Este es un proyecto académico que es la versión en Python del original en PHP. Realiza un registro de usuarios con envío de correo de confirmación usando SMTP de Gmail y almacenamiento en base de datos MySQL.

## 📋 Requisitos

- Python 3.7+
- pip (gestor de paquetes de Python)

## 🚀 Instalación

### 1. Clonar o descargar el proyecto
```bash
cd proyecto_python
```

### 2. Crear un entorno virtual (recomendado)
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## ⚙️ Configuración

### 1. Editar `config.py`
Actualiza los siguientes valores con tus propias credenciales:

```python
DB_CONFIG = {
    'host': 'tu_host_db',
    'user': 'tu_usuario_db',
    'password': 'tu_contraseña_db',
    'database': 'tu_base_datos'
}

SMTP_CONFIG = {
    'host': 'smtp.gmail.com',
    'port': 587,
    'sender_email': 'tu_correo@gmail.com',
    'sender_password': 'tu_contraseña_o_app_password',
    'sender_name': 'Tu Nombre'
}

SECRET_KEY = 'una_clave_secreta_fuerte'
```

### 2. Preparar la base de datos
La tabla `usuarios` debe tener la siguiente estructura:

```sql
CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    correo VARCHAR(255) UNIQUE NOT NULL,
    contrasenia VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Imagen adjunta (opcional)
- Coloca la imagen `xd.jpg` en la carpeta `static/` para que se adjunte en los correos

## 🏃 Ejecución

### Iniciar la aplicación
```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 📁 Estructura del Proyecto

```
proyecto_python/
├── app.py                 # Aplicación principal (Flask)
├── config.py              # Configuración de BD y SMTP
├── requirements.txt       # Dependencias de Python
├── README.md              # Este archivo
├── templates/
│   └── index.html         # Formulario de registro
└── static/
    └── xd.jpg            # Imagen para adjuntar (opcional)
```

## 🔑 Características Principales

✅ **Registro de Usuarios**: Formulario HTML simple para capturar correo y contraseña
✅ **Hasheo de Contraseña**: Usa werkzeug para encriptar las contraseñas
✅ **Envío de Correos**: Utiliza SMTP de Gmail para enviar confirmaciones
✅ **Base de Datos**: Almacena usuarios en MySQL
✅ **Validación**: Valida entrada de datos y maneja errores
✅ **Interfaz Responsiva**: Diseño similar al original PHP

## 🔐 Consideraciones de Seguridad

⚠️ **IMPORTANTE**: Este es un proyecto académico. En producción:
- Nunca guardes credenciales en archivos de código
- Usa variables de entorno con un archivo `.env`
- Implementa HTTPS
- Valida y sanitiza todas las entradas
- Usa tokens de acceso en lugar de contraseñas directas

### Ejemplo con variables de entorno:
```python
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}
```

## 📧 Gmail con contraseña de aplicación

Si usas Gmail con 2FA habilitado:
1. Ve a https://myaccount.google.com/apppasswords
2. Selecciona "Mail" y "Windows"
3. Google te dará una contraseña de 16 caracteres
4. Usa esa contraseña en `config.py`

## 🐛 Solución de Problemas

### Error: "Access denied for user"
- Verifica que las credenciales de BD en `config.py` sean correctas

### Error: "SMTP authentication failed"
- Verifica el correo y contraseña de Gmail
- Si usas 2FA, asegúrate de usar una contraseña de aplicación

### Error: "Tabla 'usuarios' no existe"
- Ejecuta el SQL para crear la tabla en tu base de datos

### Conexión rechazada en puerto 5000
- Es posible que el puerto esté en uso. Cambia el puerto en `app.py`:
```python
app.run(debug=True, host='localhost', port=5001)
```

## 📝 Notas

- El proyecto mantiene el mismo flujo y funcionalidad del original en PHP
- Los mensajes de error y éxito son mostrados al usuario en tiempo real
- Se incluye un spinner de carga para mejor UX

## 🎓 Propósito Educativo

Este proyecto fue creado con fines académicos para demostrar conceptos de:
- Formularios web y validación
- Conexión a bases de datos
- Envío de correos SMTP
- Seguridad (hasheo de contraseñas)
- Desarrollo web con Python (Flask)

## 📞 Contacto

Proyecto realizado para la clase de Seguridad de la Información - UACJ

---

**¡Fuiste víctima de una bromita cibernética! 👻**
