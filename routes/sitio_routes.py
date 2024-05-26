from flask import request, jsonify
from flask_jwt_extended import jwt_required
from db.db import app, db
from models.sitio import Sitio

@app.route('/sitios', methods=['GET'])
def get_sitios():
    sitios = Sitio.query.all()
    result = [{'id': sitio.id, 'nombre': sitio.nombre, 'categoria': sitio.categoria, 'descripcion': sitio.descripcion, 'ubicacion': sitio.ubicacion, 'abierto': sitio.abierto} for sitio in sitios]
    return jsonify(result), 200

@app.route('/sitios', methods=['POST'])
@jwt_required()
def add_sitio():
    data = request.get_json()
    new_sitio = Sitio(nombre=data['nombre'], categoria=data['categoria'], descripcion=data['descripcion'], ubicacion=data['ubicacion'], abierto=data['abierto'])
    db.session.add(new_sitio)
    db.session.commit()
    return jsonify(message='Sitio created successfully'), 201
