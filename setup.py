#!/usr/bin/env python3
"""
Script para configurar y probar el proyecto
"""

import sys
import os
from pathlib import Path

def test_database_connection():
    """Prueba la conexión a la base de datos"""
    print("\n🔍 Probando conexión a base de datos...")
    try:
        import mysql.connector
        import config
        
        connection = mysql.connector.connect(**config.DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        cursor.close()
        connection.close()
        
        print("✅ Conexión a BD exitosa")
        return True
    except Exception as e:
        print(f"❌ Error de conexión a BD: {e}")
        return False


def test_smtp_connection():
    """Prueba la conexión SMTP"""
    print("\n🔍 Probando conexión SMTP...")
    try:
        import smtplib
        import config
        
        server = smtplib.SMTP(config.SMTP_CONFIG['host'], config.SMTP_CONFIG['port'])
        server.starttls()
        server.login(config.SMTP_CONFIG['sender_email'], config.SMTP_CONFIG['sender_password'])
        server.quit()
        
        print("✅ Conexión SMTP exitosa")
        return True
    except Exception as e:
        print(f"❌ Error de conexión SMTP: {e}")
        print("   Verifica que:")
        print("   - La contraseña sea correcta")
        print("   - Si usas Gmail con 2FA, usa una contraseña de aplicación")
        print("   - La dirección de correo sea correcta")
        return False


def create_tables():
    """Crea las tablas necesarias en la BD"""
    print("\n🔨 Creando tablas en la base de datos...")
    try:
        import mysql.connector
        import config
        
        connection = mysql.connector.connect(**config.DB_CONFIG)
        cursor = connection.cursor()
        
        # Crear tabla usuarios
        sql = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT PRIMARY KEY AUTO_INCREMENT,
            correo VARCHAR(255) UNIQUE NOT NULL,
            contrasenia VARCHAR(255) NOT NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()
        
        print("✅ Tablas creadas/verificadas exitosamente")
        return True
    except Exception as e:
        print(f"❌ Error creando tablas: {e}")
        return False


def main():
    """Función principal"""
    print("=" * 50)
    print("🚀 CONFIGURACIÓN DEL PROYECTO PYTHON")
    print("=" * 50)
    
    # Verificar que los archivos de configuración existan
    if not os.path.exists('config.py'):
        print("❌ No se encontró config.py")
        return
    
    # Pruebas
    db_ok = test_database_connection()
    smtp_ok = test_smtp_connection()
    
    if db_ok:
        tables_ok = create_tables()
    else:
        tables_ok = False
    
    # Resumen
    print("\n" + "=" * 50)
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 50)
    print(f"Base de Datos: {'✅ OK' if db_ok else '❌ ERROR'}")
    print(f"SMTP: {'✅ OK' if smtp_ok else '❌ ERROR'}")
    print(f"Tablas: {'✅ OK' if tables_ok else '⏭️  PENDIENTE' if db_ok else '❌ ERROR'}")
    print("=" * 50)
    
    if db_ok and smtp_ok and tables_ok:
        print("\n✅ ¡Proyecto listo para usar!")
        print("   Ejecuta: python app.py")
    else:
        print("\n⚠️  Revisa los errores arriba antes de continuar")


if __name__ == '__main__':
    main()
