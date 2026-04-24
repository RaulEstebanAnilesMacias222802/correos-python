"""
Pruebas unitarias para la aplicación
"""

import unittest
import sys
from pathlib import Path

# Agregar el directorio actual al path
sys.path.insert(0, str(Path(__file__).parent))

from app import app
from werkzeug.security import check_password_hash, generate_password_hash


class TestApp(unittest.TestCase):
    """Pruebas para la aplicación Flask"""
    
    def setUp(self):
        """Configurar antes de cada prueba"""
        self.app = app
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
    
    def test_index_page_loads(self):
        """Verificar que la página principal carga"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ConectaUACJ', response.data)
    
    def test_api_status(self):
        """Verificar endpoint de estado"""
        response = self.client.get('/api/status')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'ok')
    
    def test_registro_sin_datos(self):
        """Verificar que registro sin datos falla"""
        response = self.client.post('/registro', data={})
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data['success'])
    
    def test_registro_sin_correo(self):
        """Verificar que registro sin correo falla"""
        response = self.client.post('/registro', data={
            'contrasenia': 'test123'
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data['success'])
    
    def test_registro_sin_contrasenia(self):
        """Verificar que registro sin contraseña falla"""
        response = self.client.post('/registro', data={
            'correo': 'test@example.com'
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertFalse(data['success'])
    
    def test_password_hash(self):
        """Verificar que el hash de contraseña funciona"""
        password = "test123"
        hash_pwd = generate_password_hash(password)
        
        # Verificar que el hash es diferente a la contraseña
        self.assertNotEqual(hash_pwd, password)
        
        # Verificar que se puede validar correctamente
        self.assertTrue(check_password_hash(hash_pwd, password))
        
        # Verificar que una contraseña diferente no coincide
        self.assertFalse(check_password_hash(hash_pwd, "wrongpassword"))


class TestPasswordSecurity(unittest.TestCase):
    """Pruebas de seguridad de contraseñas"""
    
    def test_hash_diferente_cada_vez(self):
        """Verificar que el hash es diferente cada vez"""
        password = "test123"
        hash1 = generate_password_hash(password)
        hash2 = generate_password_hash(password)
        
        # Los hashes deben ser diferentes (se usan salts aleatorios)
        self.assertNotEqual(hash1, hash2)
        
        # Pero ambos deben validar la misma contraseña
        self.assertTrue(check_password_hash(hash1, password))
        self.assertTrue(check_password_hash(hash2, password))
    
    def test_hash_fuerte(self):
        """Verificar que el hash es lo suficientemente fuerte"""
        password = "test123"
        hash_pwd = generate_password_hash(password)
        
        # El hash debe tener cierta longitud (bcrypt mínimo ~60 caracteres)
        self.assertGreater(len(hash_pwd), 50)
        
        # Debe contener el prefijo de bcrypt
        self.assertTrue(hash_pwd.startswith('pbkdf2:') or '$2' in hash_pwd)


class TestFormValidation(unittest.TestCase):
    """Pruebas de validación de formularios"""
    
    def test_email_vacio_se_rechaza(self):
        """Verificar que email vacío se rechaza"""
        self.client = app.test_client()
        response = self.client.post('/registro', data={
            'correo': '',
            'contrasenia': 'test123'
        })
        self.assertEqual(response.status_code, 400)
    
    def test_password_vacia_se_rechaza(self):
        """Verificar que contraseña vacía se rechaza"""
        self.client = app.test_client()
        response = self.client.post('/registro', data={
            'correo': 'test@example.com',
            'contrasenia': ''
        })
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    print("🧪 Ejecutando pruebas...")
    print("=" * 50)
    unittest.main(verbosity=2)
