class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        

user_1 = User("001", "jihun")
user_2 = User("002", "ghoney")

print(user_1.username)
print(user_2.id)
