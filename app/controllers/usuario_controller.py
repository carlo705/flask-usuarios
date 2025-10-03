from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.usuario_service import UsuarioService

usuario_bp = Blueprint('usuarios', __name__)
usuario_service = UsuarioService()


def admin_required():
    # simple check
    return session.get('user_rol') == 'admin'


@usuario_bp.route('/admin')
def panel():
    if not session.get('user_id'):
        flash('Debe iniciar sesión primero', 'error')
        return redirect(url_for('auth.login'))
    usuarios = usuario_service.listar_usuarios()
    return render_template('usuario/index.html', usuarios=usuarios)


@usuario_bp.route('/usuario/crear', methods=['GET', 'POST'])
def crear():
    if not session.get('user_id') or not admin_required():
        flash('Acceso no autorizado', 'error')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'email': request.form.get('email'),
            'password': request.form.get('password'),
            'rol': request.form.get('rol')
        }
        resultado = usuario_service.crear_usuario(datos)
        if resultado['success']:
            flash('Usuario creado exitosamente', 'success')
            return redirect(url_for('usuarios.panel'))
        else:
            for err in resultado['errores']:
                flash(err, 'error')

    return render_template('usuario/crear.html')


@usuario_bp.route('/usuario/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if not session.get('user_id') or not admin_required():
        flash('Acceso no autorizado', 'error')
        return redirect(url_for('auth.login'))

    usuario = usuario_service.obtener_usuario(id)
    if not usuario:
        flash('Usuario no encontrado', 'error')
        return redirect(url_for('usuarios.panel'))

    if request.method == 'POST':
        datos = {
            'nombre': request.form.get('nombre'),
            'email': request.form.get('email'),
            'password': request.form.get('password'),
            'rol': request.form.get('rol')
        }
        resultado = usuario_service.actualizar_usuario(id, datos)
        if resultado['success']:
            flash('Usuario actualizado exitosamente', 'success')
            return redirect(url_for('usuarios.panel'))
        else:
            for err in resultado['errores']:
                flash(err, 'error')

    return render_template('usuario/editar.html', usuario=usuario)


@usuario_bp.route('/usuario/<int:id>')
def ver(id):
    if not session.get('user_id'):
        flash('Acceso no autorizado', 'error')
        return redirect(url_for('auth.login'))

    usuario = usuario_service.obtener_usuario(id)
    if not usuario:
        flash('Usuario no encontrado', 'error')
        return redirect(url_for('usuarios.panel'))

    return render_template('usuario/ver.html', usuario=usuario)


@usuario_bp.route('/usuario/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    if not session.get('user_id') or not admin_required():
        flash('Acceso no autorizado', 'error')
        return redirect(url_for('auth.login'))

    resultado = usuario_service.eliminar_usuario(id)
    if resultado['success']:
        flash('Usuario eliminado exitosamente', 'success')
    else:
        flash(resultado.get('error', 'Error al eliminar'), 'error')
    return redirect(url_for('usuarios.panel'))
