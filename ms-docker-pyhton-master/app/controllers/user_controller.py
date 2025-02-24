from flask import make_response, jsonify, request
from app.models.user_model import User

def get_users():
    
    return make_response(
        jsonify(
            mensagem = "Listagem de user",
            usuarios = User.get_users()
        )
    ) 

def get_user_by_id(user_id):
    return make_response(
        jsonify(
            mensagem = "Listagem de user",
            usuarios = User.get_user_by_id(user_id)
        )
    ) 

def store():
    data = request.get_json()

    name = data.get("name", "")
    email = data.get("email", "")

    if not name or not email:
        return make_response(
        jsonify(
            mensagem = "error",
            usuarios = "Os campos 'name' e 'email' são obrigatórios e não podem estar vazios."
        ), 400
    )         

    return make_response(
        jsonify(
            mensagem = "user salvo com sucesso",
            usuarios = User.store(data)
        )
    ) 