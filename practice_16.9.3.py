class PetFriends:
    def __init__(self, user_name, user_balance):
        self.user_name = user_name
        self.user_balance = user_balance

    def get_info(self):
        return f"Клиент: {self.user_name}, Баланс: {self.user_balance} руб."

u1 = PetFriends("Иван Петров", 50)

print(u1.get_info())



