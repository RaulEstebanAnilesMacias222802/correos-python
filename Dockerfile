# Dockerfile para ejecutar la aplicación en contenedores

FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de requisitos
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar archivos de la aplicación
COPY . .

# Exponer puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
