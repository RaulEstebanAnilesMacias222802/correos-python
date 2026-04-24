"""
Script para iniciar la aplicación en diferentes modos
"""

import sys
import os
from pathlib import Path

# Agregar el directorio actual al path
sys.path.insert(0, str(Path(__file__).parent))

from app import app, logger

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='Iniciar la aplicación de registro')
    parser.add_argument('--host', default='localhost', help='Host donde escuchar (default: localhost)')
    parser.add_argument('--port', type=int, default=5000, help='Puerto donde escuchar (default: 5000)')
    parser.add_argument('--debug', action='store_true', help='Ejecutar en modo debug')
    
    args = parser.parse_args()
    
    logger.info(f"🚀 Iniciando aplicación en http://{args.host}:{args.port}")
    
    app.run(
        host=args.host,
        port=args.port,
        debug=args.debug
    )
