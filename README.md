## Flash CRUD MVC

# Estructura

flask_crud_mvc/
│
├── venv/                          # Virtual environment
│
├── app/
│   ├── __init__.py               # Inicialización de la app Flask
│   ├── config.py                 # Configuración de la BD
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── producto.py           # Modelo Producto
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── producto_repository.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── producto_service.py
│   │
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── producto_controller.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── crear.html
│   │   ├── editar.html
│   │   └── ver.html
│   │
│   └── static/
│       └── css/
│           └── style.css
│
├── requirements.txt
└── run.py                        # Punto de entrada

# 1. Requisitos Previos

Python 3.8 o superior instalado
MySQL Server instalado y ejecutándose
pip (gestor de paquetes de Python)

# 2 Crear el proyecto

# Crear directorio del proyecto
mkdir flask_crud_mvc
cd flask_crud_mvc

# Crear la estructura de carpetas
mkdir -p app/{models,repositories,services,controllers,templates,static/css}

#3 