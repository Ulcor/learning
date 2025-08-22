class Human:
    def __init__(self, username, first_name, last_name):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.username}" - {self.first_name}


new_user = Human("@123","test_user","test")

print(new_user.username)
print(new_user.first_name)
print(new_user.last_name)
