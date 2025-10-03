from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuración
    app.config.from_object('app.config.Config')
    
    # Blueprints para usuarios y autenticación
    from app.controllers.usuario_controller import usuario_bp
    from app.controllers.auth_controller import auth_bp
    app.register_blueprint(usuario_bp)
    app.register_blueprint(auth_bp)

    # Configuración de secret key (ya cargado desde Config)
    app.secret_key = app.config.get('SECRET_KEY')
    
    return app