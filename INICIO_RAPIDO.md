# 🚀 INICIO RÁPIDO

## Paso 1: Preparar el entorno

```bash
# Navegar a la carpeta del proyecto
cd proyecto_python

# Crear entorno virtual (Windows)
python -m venv venv
venv\Scripts\activate

# O en macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

## Paso 2: Instalar dependencias

```bash
pip install -r requirements.txt
```

## Paso 3: Configurar credenciales

Edita el archivo `config.py` con tus datos:

```python
DB_PATH = 'database.db'

SMTP_CONFIG = {
    'host': 'smtp.gmail.com',
    'port': 465,
    'sender_email': 'tu_correo@gmail.com',
    'sender_password': 'tu_contraseña_app',  # Si usas 2FA en Gmail
    'sender_name': 'Tu Nombre'
}
```

## Paso 4: Probar la configuración

```bash
python setup.py
```

Este comando verifica:
- ✅ Conexión a base de datos
- ✅ Conexión SMTP
- ✅ Crea las tablas necesarias

## Paso 5: Ejecutar la aplicación

```bash
# Opción 1: Usando run.py
python run.py

# Opción 2: Directamente
python app.py

# Opción 3: Con opciones personalizadas
python run.py --port 8000 --debug
```

## Paso 6: Abrir en el navegador

Abre tu navegador y ve a:
```
http://localhost:5000
```

---

## 📝 Ejemplo de Uso Completo

```bash
# 1. Clonar/descargar y entrar a la carpeta
cd proyecto_python

# 2. Crear virtual env
python -m venv venv

# 3. Activar env (Windows)
venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Editar config.py con tus credenciales

# 6. Probar configuración
python setup.py

# 7. Iniciar la app
python app.py

# 8. Abrir navegador en http://localhost:5000
```

---

## 🔍 Solución de Problemas Rápidos

### Error: "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### Error: "Access denied for user"
Verifica el usuario y contraseña en `config.py`

### Error: "SMTP authentication failed"
```
- Verifica que el correo sea correcto
- Si usas Gmail con 2FA, usa contraseña de aplicación
- No es tu contraseña de Gmail, es la app password
```

### Error: "Tabla usuarios no existe"
```bash
python setup.py
# Esto creará las tablas automáticamente
```

### El puerto 5000 está en uso
```bash
python run.py --port 8000
```

---

## 📧 Credenciales del Proyecto Original

Las credenciales visibles en el código son:
- **Gmail**: soporteuacjcast@gmail.com
- **BD**: if0_41739853_uacj en sql201.infinityfree.com

**⚠️ IMPORTANTE**: Cambia estas credenciales por las tuyas propias en producción.

---

## 📁 Archivos Importantes

| Archivo | Propósito |
|---------|-----------|
| `app.py` | Aplicación principal |
| `config.py` | Configuración (EDITAR) |
| `setup.py` | Script de configuración |
| `requirements.txt` | Dependencias de Python |
| `templates/index.html` | Formulario de registro |
| `static/` | Imágenes y CSS |

---

## ✅ Checklist antes de ir a Producción

- [ ] Cambié `config.py` con mis credenciales
- [ ] Ejecuté `python setup.py` y todas las pruebas pasaron
- [ ] La BD está creada y accesible
- [ ] El correo SMTP funciona correctamente
- [ ] Puse una imagen `xd.jpg` en `static/` (opcional)
- [ ] Probé el formulario y recibí el correo

---

¡Listo! La aplicación debería estar funcionando. 🎉

Para más detalles, lee `README.md` o `COMPARACION.md`.
