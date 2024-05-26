from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from db.db import app
from models.usuario import Usuario

@app.route('/usuarios', methods=['GET'])
@jwt_required()
def get_usuarios():
    users = Usuario.query.all()
    result = [{'id': user.id, 'email': user.email, 'username': user.username} for user in users]
    return jsonify(result), 200
