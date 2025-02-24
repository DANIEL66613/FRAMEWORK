class User:
    # Simulação de um banco de dados
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
        """Adiciona um novo usuário à lista."""
        # Garante que o email seja único
        if any(user["email"] == data["email"] for user in cls.users):
            return {"error": "Email already exists"}

        # Garante que o ID seja único
        new_id = max(user["id"] for user in cls.users) + 1 if cls.users else 1

        new_user = {
            "id": new_id,
            "name": data["name"],
            "email": data["email"]
        }

        cls.users.append(new_user)
        return new_user  # Retorna o usuário recém-criado

    @classmethod
    def update(cls, user_id, data):
        """Atualiza um usuário existente."""
        for user in cls.users:
            if user["id"] == user_id:
                # Atualiza apenas os campos fornecidos
                user.update({k: v for k, v in data.items() if k in user})
                return user  # Retorna o usuário atualizado
        return {"error": "User not found"}

    @classmethod
    def delete(cls, user_id):
        """Remove um usuário pelo ID."""
        for i, user in enumerate(cls.users):
            if user["id"] == user_id:
                del cls.users[i]
                return {"message": "User deleted successfully"}
        return {"error": "User not found"}
