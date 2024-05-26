from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from db.db import app, db
from models.critica import Critica

@app.route('/criticas', methods=['GET'])
def get_criticas():
    criticas = Critica.query.all()
    result = [{'id': critica.id, 'contenido': critica.contenido, 'fechayhora': critica.fechayhora, 'calificacion': critica.calificacion, 'id_usuario': critica.id_usuario, 'id_sitio': critica.id_sitio} for critica in criticas]
    return jsonify(result), 200

@app.route('/criticas', methods=['POST'])
@jwt_required()
def add_critica():
    data = request.get_json()
    current_user = get_jwt_identity()
    new_critica = Critica(contenido=data['contenido'], fechayhora=data['fechayhora'], calificacion=data['calificacion'], id_usuario=current_user['id'], id_sitio=data['id_sitio'])
    db.session.add(new_critica)
    db.session.commit()
    return jsonify(message='Critica created successfully'), 201
