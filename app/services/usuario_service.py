from app.repositories.usuario_repository import UsuarioRepository
from app.models.usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()

    def listar_usuarios(self):
        return self.repo.obtener_todos()

    def obtener_usuario(self, usuario_id):
        return self.repo.obtener_por_id(usuario_id)

    def autenticar(self, email, password):
        usuario = self.repo.obtener_por_email(email)
        if not usuario:
            return None
        # Autenticación por texto plano (proyecto de prueba)
        # Comprueba si la contraseña proporcionada coincide exactamente
        # con el valor almacenado en la base de datos.
        if usuario.password == password:
            return usuario
        return None

    def crear_usuario(self, datos):
        errores = []
        nombre = datos.get('nombre', '').strip()
        email = datos.get('email', '').strip()
        password = datos.get('password', '')
        rol = datos.get('rol', 'usuario')

        if not nombre:
            errores.append('El nombre es obligatorio')
        if not email:
            errores.append('El email es obligatorio')
        if not password:
            errores.append('La contraseña es obligatoria')

        # comprobar email único
        if self.repo.obtener_por_email(email):
            errores.append('Ya existe un usuario con ese email')

        if errores:
            return {'success': False, 'errores': errores}

        # Guardar la contraseña tal cual (texto plano) para pruebas
        usuario = Usuario(nombre=nombre, email=email, password=password, rol=rol)
        usuario_id = self.repo.crear(usuario)
        return {'success': True, 'id': usuario_id}

    def actualizar_usuario(self, usuario_id, datos):
        usuario_existente = self.repo.obtener_por_id(usuario_id)
        if not usuario_existente:
            return {'success': False, 'errores': ['Usuario no encontrado']}

        errores = []
        nombre = datos.get('nombre', '').strip()
        email = datos.get('email', '').strip()
        password = datos.get('password', None)
        rol = datos.get('rol', usuario_existente.rol)

        if not nombre:
            errores.append('El nombre es obligatorio')
        if not email:
            errores.append('El email es obligatorio')

        # Si el email cambia, verificar unicidad
        si = self.repo.obtener_por_email(email)
        if si and si.id != usuario_id:
            errores.append('Otro usuario ya usa ese email')

        if errores:
            return {'success': False, 'errores': errores}

        # Mantener password si no se proporciona
        if password:
            new_password = password
        else:
            new_password = usuario_existente.password

        usuario = Usuario(id=usuario_id, nombre=nombre, email=email, password=new_password, rol=rol)
        self.repo.actualizar(usuario)
        return {'success': True}

    def eliminar_usuario(self, usuario_id):
        existe = self.repo.obtener_por_id(usuario_id)
        if not existe:
            return {'success': False, 'error': 'Usuario no encontrado'}
        self.repo.eliminar(usuario_id)
        return {'success': True}
