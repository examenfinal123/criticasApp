from db.db import db

class Critica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    fechayhora = db.Column(db.DateTime, nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_sitio = db.Column(db.Integer, db.ForeignKey('sitio.id'), nullable=False)
