class User:

    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ]

    @classmethod
    def get_users(cls):
        """Retorna todos os usuários cadastrados."""
        return cls.users

    @classmethod
    def get_user_by_id(cls, user_id):
        """Retorna um usuário pelo ID."""
        for user in cls.users:
            if user["id"] == user_id:
                return user
        return None
    
    @classmethod
    def store(cls, data):
        
        if any(user["email"] == data["email"] for user in cls.users):
            return {"error": "Email já existe"}

        new_id = max(user["id"] for user in cls.users) + 1 if cls.users else 1

        new_user = {
            "id": new_id,
            "name": data["name"],
            "email": data["email"]
        }

        cls.users.append(new_user)
        return new_user 

    @classmethod
    def update(cls, user_id, data):
        for user in cls.users:
            if user["id"] == user_id:
                # atualiza só os campos que forem fornecidos
                user.update({k: v for k, v in data.items() if k in user})
                return user  
        return {"error": "Usuario nao encontrado"}

    @classmethod
    def delete(cls, user_id):
        for i, user in enumerate(cls.users):
            if user["id"] == user_id:
                del cls.users[i]
                return {"message": "Usuario deletado! "}
        return {"error": "Usuarui nao encontrado"}
