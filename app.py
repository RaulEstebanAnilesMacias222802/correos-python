from flask import Flask, render_template, request, jsonify
import mysql.connector
from werkzeug.security import generate_password_hash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import config
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_db_connection():
    """Conectar a la base de datos"""
    try:
        connection = mysql.connector.connect(**config.DB_CONFIG)
        return connection
    except mysql.connector.Error as err:
        logger.error(f"Error de conexión a BD: {err}")
        raise


def send_confirmation_email(email):
    """Enviar correo de confirmación de registro"""
    try:
        # Configurar servidor SMTP
        server = smtplib.SMTP(config.SMTP_CONFIG['host'], config.SMTP_CONFIG['port'])
        server.starttls()
        server.login(config.SMTP_CONFIG['sender_email'], config.SMTP_CONFIG['sender_password'])
        
        # Crear mensaje
        mensaje = MIMEMultipart('related')
        mensaje['Subject'] = 'Confirmacion de Registro'
        mensaje['From'] = f"{config.SMTP_CONFIG['sender_name']} <{config.SMTP_CONFIG['sender_email']}>"
        mensaje['To'] = email
        
        # HTML del correo
        html_content = """
        <table border='0' cellpadding='0' cellspacing='0' width='100%' style='background-color: #f4f4f4; padding: 20px;'>
        <tr>
        <td align='center'>
        <table border='0' cellpadding='0' cellspacing='0' width='600' style='background-color: #ffffff; border: 1px solid #dddddd;'>
        <tr>
        <td align='center' style='padding: 20px 0; background-color: #d9534f;'>
        <h1 style='color: #ffffff; font-family: Arial, sans-serif; margin: 0;'>¡ATENCIÓN! 👻</h1>
        </td>
        </tr>
        <tr>
        <td style='padding: 30px; font-family: Arial, sans-serif; line-height: 1.6; color: #333333;'>
        <p style='font-size: 18px; font-weight: bold;'>Has caído en una simulación de broma cibernética.</p>
        <p>Esta es una actividad académica para la clase de <b>Seguridad de la Información</b>. Tus datos no han sido vulnerados, pero este ejercicio sirve para recordarte que siempre debes verificar la URL antes de ingresar tus credenciales.</p>
        </td>
        </tr>
        <tr>
        <td align='center' style='padding: 0 10px 30px 10px;'>
        <img src='cid:xd' alt='Broma' width='500' style='display: block; width: 100%; max-width: 500px; height: auto; border: 0;'>
        </td>
        </tr>
        <tr>
        <td align='center' style='padding: 20px; background-color: #f8f8f8; font-family: Arial, sans-serif; font-size: 12px; color: #999999;'>
        No respondas a este correo. <br>
        <b>Entorno de Desarrollo - UACJ Ciudad Juárez</b>
        </td>
        </tr>
        </table>
        </td>
        </tr>
        </table>
        """
        
        # Agregar contenido HTML
        msg_alternative = MIMEMultipart('alternative')
        mensaje.attach(msg_alternative)
        
        msg_text = MIMEText('¡Fuiste víctima de una bromita cibernética! Esto es una prueba de seguridad.', 'plain')
        msg_html = MIMEText(html_content, 'html')
        
        msg_alternative.attach(msg_text)
        msg_alternative.attach(msg_html)
        
        # Adjuntar imagen (si existe)
        try:
            with open('static/xd.jpg', 'rb') as attachment:
                image = MIMEImage(attachment.read())
                image.add_header('Content-ID', '<xd>')
                image.add_header('Content-Disposition', 'inline', filename='xd.jpg')
                mensaje.attach(image)
        except FileNotFoundError:
            logger.warning("Imagen xd.jpg no encontrada")
        
        # Enviar correo
        server.send_message(mensaje)
        server.quit()
        
        return True, "Correo enviado exitosamente"
        
    except Exception as e:
        logger.error(f"Error enviando correo: {e}")
        return False, f"Error al enviar correo: {str(e)}"


@app.route('/')
def index():
    """Página de inicio con formulario de login"""
    return render_template('index.html')


@app.route('/registro', methods=['POST'])
def registro():
    """Procesar registro de usuario"""
    
    # Validar que los datos existan
    correo = request.form.get('correo', '').strip()
    contrasenia = request.form.get('contrasenia', '').strip()
    
    if not correo or not contrasenia:
        return jsonify({'success': False, 'message': 'Por favor completa todos los campos'}), 400
    
    try:
        # Conectar a base de datos
        connection = get_db_connection()
        cursor = connection.cursor()
        
        # Hash de la contraseña
        contrasenia_hash = generate_password_hash(contrasenia)
        
        # Insertar usuario
        query = "INSERT INTO usuarios (correo, contrasenia) VALUES (%s, %s)"
        cursor.execute(query, (correo, contrasenia_hash))
        connection.commit()
        
        cursor.close()
        connection.close()
        
        logger.info(f"Usuario registrado: {correo}")
        
        # Enviar correo de confirmación
        email_sent, email_message = send_confirmation_email(correo)
        
        if email_sent:
            return jsonify({
                'success': True, 
                'message': '¡Registro exitoso! Revisa tu correo electrónico para más información.'
            }), 200
        else:
            return jsonify({
                'success': True,
                'message': f'Registro exitoso, pero hubo un problema al enviar el correo: {email_message}'
            }), 200
            
    except mysql.connector.Error as err:
        logger.error(f"Error de base de datos: {err}")
        
        if err.errno == 1062:  # Duplicate entry
            return jsonify({
                'success': False, 
                'message': 'Este correo ya está registrado'
            }), 400
        else:
            return jsonify({
                'success': False, 
                'message': 'Error en la base de datos'
            }), 500
            
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        return jsonify({
            'success': False, 
            'message': 'Error al procesar el registro'
        }), 500


@app.route('/api/status')
def status():
    """Verificar estado de la aplicación"""
    return jsonify({'status': 'ok', 'version': '1.0'})


if __name__ == '__main__':
    app.run(debug=config.DEBUG, host='localhost', port=5000)
