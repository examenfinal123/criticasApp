from db.db import db

class Sitio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    ubicacion = db.Column(db.String(200), nullable=False)
    abierto = db.Column(db.Boolean, default=True)
    criticas = db.relationship('Critica', backref='sitio', lazy=True)
