from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.usuario_service import UsuarioService

auth_bp = Blueprint('auth', __name__)
usuario_service = UsuarioService()


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        usuario = usuario_service.autenticar(email, password)
        if usuario:
            session['user_id'] = usuario.id
            session['user_nombre'] = usuario.nombre
            session['user_rol'] = usuario.rol
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('usuarios.panel'))
        else:
            flash('Credenciales inválidas', 'error')
    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada', 'success')
    return redirect(url_for('auth.login'))
