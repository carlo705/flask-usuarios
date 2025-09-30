from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuración
    app.config.from_object('app.config.Config')
    
    # Registrar blueprints
    from app.controllers.producto_controller import producto_bp
    app.register_blueprint(producto_bp)
    
    return app