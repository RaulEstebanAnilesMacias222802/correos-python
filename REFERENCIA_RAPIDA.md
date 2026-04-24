# Referencia Rápida - Proyecto Python

## 📚 Documentación Disponible

- **README.md** - Documentación completa del proyecto
- **INICIO_RAPIDO.md** - Pasos para empezar inmediatamente
- **COMPARACION.md** - Diferencias entre PHP y Python
- **Este archivo** - Referencia rápida

---

## 🏗️ Estructura del Proyecto

```
proyecto_python/
├── app.py                 # Aplicación Flask principal
├── config.py              # Configuración (EDITAR)
├── requirements.txt       # Dependencias de Python
├── setup.py               # Script de configuración
├── run.py                 # Script para iniciar la app
├── test_app.py            # Pruebas unitarias
├── Dockerfile             # Para Docker
├── docker-compose.yml     # Docker Compose
├── .gitignore             # Para Git
├── .env.example           # Ejemplo de variables de entorno
├── README.md              # Documentación completa
├── INICIO_RAPIDO.md       # Guía rápida
├── COMPARACION.md         # Comparación PHP vs Python
├── templates/
│   └── index.html         # Formulario de registro
└── static/
    └── xd.jpg            # Imagen (opcional)
```

---

## 🔧 Configuración Inicial

### 1. Crear Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Editar config.py
```python
DB_CONFIG = {
    'host': 'tu_host_mysql',
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'database': 'tu_base_datos'
}

SMTP_CONFIG = {
    'host': 'smtp.gmail.com',
    'port': 587,
    'sender_email': 'tu_correo@gmail.com',
    'sender_password': 'app_password',  # Si tienes 2FA
    'sender_name': 'Tu Nombre'
}
```

### 4. Crear Tablas
```bash
python setup.py
```

### 5. Ejecutar Aplicación
```bash
python app.py
# Abrir: http://localhost:5000
```

---

## 📝 Comandos Útiles

```bash
# Instalar un paquete específico
pip install nombre_paquete

# Ver paquetes instalados
pip list

# Actualizar pip
pip install --upgrade pip

# Ejecutar pruebas
python -m pytest test_app.py
python test_app.py

# Ejecutar con puerto diferente
python run.py --port 8000

# Ejecutar en modo debug
python run.py --debug

# Congelar dependencias (para reproducibilidad)
pip freeze > requirements.txt

# Desactivar virtual environment
deactivate
```

---

## 🐳 Docker

### Construir y ejecutar con Docker
```bash
# Construir imagen
docker build -t proyecto-python .

# Ejecutar contenedor
docker run -p 5000:5000 proyecto-python

# O usar Docker Compose
docker-compose up
```

---

## 🔌 Rutas de la Aplicación

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Página principal con formulario |
| `/registro` | POST | Procesa registro de usuarios |
| `/api/status` | GET | Verifica estado de la app |

---

## 📧 Integración Gmail

### Con autenticación normal
1. Usuario: tu_correo@gmail.com
2. Contraseña: tu_contraseña_gmail

### Con 2FA (recomendado)
1. Habilitar 2FA en tu cuenta Google
2. Ir a: https://myaccount.google.com/apppasswords
3. Seleccionar "Mail" y "Windows"
4. Copiar contraseña de 16 caracteres
5. Usar esa contraseña en config.py

---

## 🧪 Pruebas

### Ejecutar todas las pruebas
```bash
python test_app.py
```

### Pruebas incluidas
- ✅ Carga de página principal
- ✅ Endpoint de estado
- ✅ Validación de formulario vacío
- ✅ Validación de email vacío
- ✅ Validación de contraseña vacía
- ✅ Funcionalidad de hash de contraseña
- ✅ Seguridad del hash

---

## 🐛 Debugging

### Modo Debug en Flask
```python
# En app.py o config.py
DEBUG = True
```

### Logging
```python
import logging
logger = logging.getLogger(__name__)
logger.info("Mensaje")
logger.error("Error")
```

### Ver logs de la aplicación
La aplicación registra automáticamente:
- Usuarios registrados
- Errores de base de datos
- Errores de correo
- Intentos fallidos

---

## 📊 Base de Datos

### Tabla usuarios
```sql
CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    correo VARCHAR(255) UNIQUE NOT NULL,
    contrasenia VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Querys útiles
```sql
-- Ver usuarios registrados
SELECT * FROM usuarios;

-- Contar usuarios
SELECT COUNT(*) FROM usuarios;

-- Buscar por correo
SELECT * FROM usuarios WHERE correo = 'correo@example.com';

-- Eliminar usuario (cuidado!)
DELETE FROM usuarios WHERE id = 1;
```

---

## 🔐 Seguridad

### Lo que hace bien:
- ✅ Hash de contraseñas con bcrypt
- ✅ SQL Injection prevention (placeholders)
- ✅ Validación de entrada
- ✅ Manejo de excepciones

### Mejoras recomendadas para producción:
- [ ] Usar HTTPS
- [ ] Implementar CSRF tokens
- [ ] Rate limiting
- [ ] Validación de email (enviar token)
- [ ] Usar variables de entorno (.env)
- [ ] Logs de auditoría
- [ ] Session management
- [ ] CORS si es necesario

---

## 🚀 Deploy

### Heroku
```bash
# Crear archivo Procfile
echo "web: gunicorn app:app" > Procfile

# Instalar gunicorn
pip install gunicorn

# Empujar a Heroku
git push heroku main
```

### AWS Lambda + RDS
1. Preparar función Lambda con Flask
2. Usar RDS para MySQL
3. Configurar API Gateway

### PythonAnywhere
1. Subir archivos
2. Crear web app
3. Apuntar a app.py
4. Configurar variables de entorno

---

## 📚 Recursos

- **Flask Docs**: https://flask.palletsprojects.com
- **MySQL Connector Python**: https://dev.mysql.com/doc/connector-python/en/
- **Werkzeug**: https://werkzeug.palletsprojects.com
- **SMTP Python**: https://docs.python.org/3/library/smtplib.html

---

## 📞 Errores Comunes

| Error | Solución |
|-------|----------|
| `ModuleNotFoundError: No module named 'flask'` | `pip install -r requirements.txt` |
| `Access denied for user` | Verifica DB_CONFIG en config.py |
| `SMTP authentication failed` | Usa contraseña de app de Gmail |
| `Connection refused` | Verifica que BD esté accesible |
| `Port already in use` | `python run.py --port 8000` |
| `Tabla no existe` | `python setup.py` |

---

## ✨ Características Implementadas

### Backend (Python + Flask)
- ✅ Enrutamiento de páginas
- ✅ Procesamiento de formularios
- ✅ Conexión a MySQL
- ✅ Hash de contraseñas
- ✅ Envío de correos SMTP
- ✅ Manejo de excepciones
- ✅ Validación de datos
- ✅ API REST (JSON)

### Frontend (HTML + CSS + JavaScript)
- ✅ Formulario responsivo
- ✅ Validación de lado cliente
- ✅ AJAX (sin recargar página)
- ✅ Mensajes de error/éxito
- ✅ Spinner de carga
- ✅ Diseño similar al original

---

## 📄 Licencia

Proyecto académico - UACJ
