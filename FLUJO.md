# Flujo de la Aplicación

## Diagrama de Flujo - Registro de Usuario

```
┌─────────────────────────────────────────────────────────────┐
│                      USUARIO                                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Abre navegador
                              ↓
┌─────────────────────────────────────────────────────────────┐
│   GET http://localhost:5000/                                 │
│   (Flask renderiza index.html)                               │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Rellena formulario
                              │ - Correo
                              │ - Contraseña
                              ↓
┌─────────────────────────────────────────────────────────────┐
│   Validación JavaScript (lado cliente)                       │
│   - ¿Está vacío?                                             │
│   - ¿Es email válido?                                        │
└─────────────────────────────────────────────────────────────┘
                              │
                    Hace clic en "Registrarse"
                              │
                              ↓
┌─────────────────────────────────────────────────────────────┐
│   POST /registro                                             │
│   (AJAX - sin recargar página)                               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ↓
┌─────────────────────────────────────────────────────────────┐
│   SERVIDOR (app.py - registro())                            │
│   1. Recibe datos POST                                       │
│   2. Valida que no estén vacíos                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ↓
┌─────────────────────────────────────────────────────────────┐
│   hash_contraseña = generate_password_hash(contraseña)      │
│   (Usa bcrypt para hashear)                                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ↓
┌─────────────────────────────────────────────────────────────┐
│   BASE DE DATOS (MySQL)                                     │
│   INSERT INTO usuarios (correo, contrasenia)                │
│   VALUES (correo, hash_contraseña)                          │
└─────────────────────────────────────────────────────────────┘
                              │
                    ¿Resultado?
                   /           \
              ✓ OK          ✗ Error
              │               │
              ↓               ↓
        ┌─────────────┐  ┌──────────────┐
        │ Guardado    │  │ Duplicado o  │
        │ exitoso     │  │ error BD     │
        └─────────────┘  └──────────────┘
              │               │
              ↓               ↓
        ┌──────────────────┐  ┌─────────────────┐
        │ send_email()     │  │ return JSON     │
        └──────────────────┘  │ error 400/500   │
              │               └─────────────────┘
              │                    │
              ↓                    ↓
        ┌──────────────────┐  ┌─────────────┐
        │ SMTP Gmail       │  │ Usuario ve  │
        │ 1. Conecta       │  │ mensaje de  │
        │ 2. Autentica     │  │ error       │
        │ 3. Prepara email │  └─────────────┘
        │ 4. Adjunta imagen│
        │ 5. Envía         │
        │ 6. Desconecta    │
        └──────────────────┘
              │
              │ ¿Correo enviado?
             / \
        ✓  /   \ ✗
          /       \
         ↓         ↓
    ┌────────┐  ┌──────────┐
    │ Éxito  │  │ Advertencia
    └────────┘  └──────────┘
         │           │
         └─────┬─────┘
              │
              ↓
    ┌──────────────────────┐
    │ return JSON success  │
    │ {                    │
    │   "success": true,   │
    │   "message": "..."   │
    │ }                    │
    └──────────────────────┘
              │
              ↓
    ┌──────────────────────────────┐
    │ JavaScript recibe respuesta  │
    │ y actualiza UI:              │
    │ - Muestra mensaje verde      │
    │ - Limpia formulario          │
    │ - Redirecciona en 3s         │
    └──────────────────────────────┘
              │
              ↓
    ┌──────────────────────────────┐
    │ Usuario ve:                  │
    │ "¡Wazaaaaa, Bromitaaaa 👻!"  │
    │ "Revisa tu correo..."        │
    └──────────────────────────────┘
              │
              │ En 3 segundos
              ↓
    ┌──────────────────────────────┐
    │ Redirecciona a:              │
    │ SharePoint UACJ              │
    └──────────────────────────────┘
```

---

## Componentes Principales

### 1. Frontend (templates/index.html)
```
┌─ HTML (estructura)
│  ├─ Formulario
│  │  ├─ Input Email
│  │  ├─ Input Password
│  │  └─ Button Submit
│  └─ Div para mensajes
│
├─ CSS (estilos)
│  ├─ Body (fondo)
│  ├─ Login container
│  ├─ Inputs
│  ├─ Botones
│  ├─ Mensajes (success/error)
│  └─ Spinner (carga)
│
└─ JavaScript (interactividad)
   ├─ Listener en formulario
   ├─ Validación
   ├─ Fetch AJAX
   ├─ Manejo de respuestas
   └─ UI updates
```

### 2. Backend (app.py)
```
┌─ Flask App
│  ├─ Rutas
│  │  ├─ GET / (render index.html)
│  │  ├─ POST /registro (procesa datos)
│  │  └─ GET /api/status (estado)
│  │
│  ├─ Funciones
│  │  ├─ get_db_connection()
│  │  │  └─ Conecta a MySQL
│  │  │
│  │  └─ send_confirmation_email(email)
│  │     ├─ Conecta a SMTP Gmail
│  │     ├─ Prepara mensaje MIME
│  │     ├─ Adjunta imagen
│  │     └─ Envía correo
│  │
│  └─ Manejo de excepciones
│     ├─ mysql.connector.Error
│     ├─ smtplib.SMTPException
│     └─ Exception general
│
└─ Logging
   └─ Registra eventos importantes
```

### 3. Configuración (config.py)
```
┌─ DB_CONFIG
│  ├─ host: servidor MySQL
│  ├─ user: usuario
│  ├─ password: contraseña
│  └─ database: base de datos
│
├─ SMTP_CONFIG
│  ├─ host: smtp.gmail.com
│  ├─ port: 587
│  ├─ sender_email: correo@gmail.com
│  ├─ sender_password: contraseña/app_password
│  └─ sender_name: nombre mostrado
│
└─ Flask Config
   ├─ SECRET_KEY: para sesiones
   └─ DEBUG: modo debug
```

### 4. Base de Datos (MySQL)
```
┌─ Tabla: usuarios
│  ├─ id (INT, PRIMARY KEY, AUTO_INCREMENT)
│  ├─ correo (VARCHAR(255), UNIQUE, NOT NULL)
│  ├─ contrasenia (VARCHAR(255), NOT NULL)
│  └─ fecha_registro (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
│
└─ Índices
   └─ UNIQUE en correo (previene duplicados)
```

---

## Flujo de Seguridad

```
Usuario escribe contraseña
           │
           ↓
JavaScript valida (lado cliente)
           │
           ↓
Envía AJAX POST a /registro
           │
           ↓
Server recibe en Python
           │
           ↓
Valida nuevamente (lado servidor) ⚠️ IMPORTANTE
           │
           ↓
generate_password_hash(contraseña)
           │
           ├─ Genera salt aleatorio
           ├─ Aplica PBKDF2 o bcrypt
           └─ Retorna hash ~60 caracteres
           │
           ↓
INSERT INTO usuarios con hash
(contraseña NUNCA se guarda en texto)
           │
           ↓
DB almacena hash
(si se roba la BD, las contraseñas están seguras)
```

---

## Manejo de Errores

```
try:
    ├─ Conectar a BD
    ├─ Ejecutar INSERT
    └─ Enviar correo
catch mysql.connector.Error:
    ├─ 1062 (Duplicate): "Correo ya registrado"
    └─ Otro: "Error en base de datos"
catch smtplib.Error:
    └─ "Error al enviar correo"
catch Exception:
    └─ "Error inesperado"
```

---

## Ciclo de Vida de una Solicitud

```
1. Cliente abre página
   ↓
2. Servidor responde con HTML + CSS + JS
   ↓
3. Cliente rellena formulario
   ↓
4. Cliente hace AJAX POST /registro
   ↓
5. Servidor recibe en app.py
   ↓
6. Valida datos
   ↓
7. Hash contraseña
   ↓
8. Inserta en BD
   ↓
9. Prepara email
   ↓
10. Conecta a SMTP
   ↓
11. Envía correo
   ↓
12. Retorna JSON al cliente
   ↓
13. JavaScript actualiza UI
   ↓
14. Usuario ve resultado
```

---

## Variables Globales y Estados

```
Frontend (JavaScript):
├─ correo (string)
├─ contrasenia (string)
├─ btnRegistro (HTMLElement)
├─ spinner (HTMLElement)
└─ mensaje (HTMLElement)

Backend (Flask):
├─ app (Flask instance)
├─ config (módulo de configuración)
└─ logger (logging instance)

Base de Datos (MySQL):
├─ usuarios.id (auto-increment)
├─ usuarios.correo (UNIQUE)
├─ usuarios.contrasenia (hashed)
└─ usuarios.fecha_registro (timestamp)
```

---

¡Este es el flujo completo de cómo funciona la aplicación!
