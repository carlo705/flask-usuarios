-- database.sql
-- Ajustado para usar la base por defecto 'flask_crud_db' (ver app/config.py)
CREATE DATABASE IF NOT EXISTS flask_crud_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE flask_crud_db;

-- Tabla usuarios con columna password para autenticación
CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  rol ENUM('admin','usuario') NOT NULL DEFAULT 'usuario'
);

INSERT INTO usuarios (nombre, email, password, rol)
VALUES ('Administrador', 'admin@example.com', 'adminpass', 'admin');

INSERT INTO usuarios (nombre, email, password, rol)
VALUES ('Usuario Demo', 'user@example.com', 'userpass', 'usuario');