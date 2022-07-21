from .models import MyUser

def register():
    username = input("Введите юзернейм: ")
    password = input("Введите пароль: ")
    MyUser.create(username=username, password=password)
    return "Пользователь успешно зарегистрирован"
    