# Flash CRUD MVC

## Estructura
# Flask Usuarios (CRUD + Login)

Aplicación de ejemplo en Flask que implementa autenticación básica (login) y un CRUD de usuarios
usando MySQL. Esta versión está pensada para pruebas locales/educativas.

## Estructura del proyecto

```
flask-crud-mvc/
├── app/
│   ├── __init__.py            # Inicialización de la app y registro de blueprints
│   ├── config.py              # Configuración (MYSQL_*, SECRET_KEY)
│   ├── controllers/           # Blueprints: auth, usuarios
│   │   ├── auth_controller.py
│   │   └── usuario_controller.py
│   ├── models/                # Modelos (Usuario)
│   │   └── usuario.py
│   ├── repositories/          # Acceso a la DB (UsuarioRepository)
│   │   └── usuario_repository.py
│   ├── services/              # Lógica de negocio (UsuarioService)
│   │   └── usuario_service.py
│   ├── templates/             # Plantillas Jinja2
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── auth/login.html
│   │   └── usuario/ (crear, editar, index, ver)
│   └── static/
│       └── css/style.css
├── database.sql               # Script para crear BD y tablas de ejemplo
├── requirements.txt
└── run.py                     # Punto de entrada
```

## Requisitos

- Python 3.8+ (se probó con 3.9)
- MySQL Server en ejecución
- pip

## Instalación rápida

1. Crear/activar virtualenv (ejemplo macOS / zsh):

```bash
python3 -m venv env
source env/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Crear la base de datos y tablas (ajusta credenciales si es necesario):

```bash
# Usa el cliente mysql y ejecuta el script
mysql -u root -p < database.sql
```

4. (Opcional) Poblar ejemplos: el script `database.sql` incluye instrucciones comentadas para insertar
	 un admin y un usuario de ejemplo (puedes usar contraseñas en texto plano para pruebas locales).

5. Ejecutar la aplicación:

```bash
# puerto 6500
env/bin/python run.py
```

6. Abrir en el navegador:

- Página de login: http://127.0.0.1:6500/login
- Panel (lista de usuarios, requiere login): http://127.0.0.1:6500/admin