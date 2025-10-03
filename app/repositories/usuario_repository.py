import pymysql
from flask import current_app
from app.models.usuario import Usuario

class UsuarioRepository:
    def _get_connection(self):
        return pymysql.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DB'],
            port=current_app.config['MYSQL_PORT'],
            cursorclass=pymysql.cursors.DictCursor
        )

    def obtener_todos(self):
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT id, nombre, email, rol FROM usuarios ORDER BY id DESC"
                cursor.execute(sql)
                rows = cursor.fetchall()
                return [Usuario.from_dict(r) for r in rows]
        finally:
            conn.close()

    def obtener_por_id(self, usuario_id):
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT id, nombre, email, password, rol FROM usuarios WHERE id = %s"
                cursor.execute(sql, (usuario_id,))
                row = cursor.fetchone()
                return Usuario.from_dict(row) if row else None
        finally:
            conn.close()

    def obtener_por_email(self, email):
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT id, nombre, email, password, rol FROM usuarios WHERE email = %s"
                cursor.execute(sql, (email,))
                row = cursor.fetchone()
                return Usuario.from_dict(row) if row else None
        finally:
            conn.close()

    def crear(self, usuario):
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO usuarios (nombre, email, password, rol) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (usuario.nombre, usuario.email, usuario.password, usuario.rol))
                conn.commit()
                return cursor.lastrowid
        finally:
            conn.close()

    def actualizar(self, usuario):
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE usuarios SET nombre = %s, email = %s, password = %s, rol = %s WHERE id = %s"
                cursor.execute(sql, (usuario.nombre, usuario.email, usuario.password, usuario.rol, usuario.id))
                conn.commit()
                return cursor.rowcount > 0
        finally:
            conn.close()

    def eliminar(self, usuario_id):
        conn = self._get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "DELETE FROM usuarios WHERE id = %s"
                cursor.execute(sql, (usuario_id,))
                conn.commit()
                return cursor.rowcount > 0
        finally:
            conn.close()
