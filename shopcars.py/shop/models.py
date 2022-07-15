#Цель проекта: реализовать CRUD действия для небольшого автосалона на классах
#Задание:
#1. Создайте класс Cars со следующими атрибутами объекта:
#● марка (строка)
#● модель (строка)
#● год выпуска (целое число)
#● объем двигателя (decimal, точность 1 знак)
# цвет (строка)
#● тип кузова (поле одиночного выбора.
#варианты: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап)
#● пробег (целое число)
#● цена (decimal, точность 2 знака)
#2. Добавьте views:
#● create для создания записей
#● listing для получения списка записей
#● retrieve для получения одной записи
#● update для обновления записей
#● delete для удаления записей
#Extra функционал:
#● Создайте urls, чтобы можно было взаимодействовать через терминал.
#● Сохранение данных в бд (json / sqlite / postgresql)
#● Сделайте комментарии
#● Сделайте лайки

#Требования к проекту:
#- код должен соответствовать PEP8
#- при использовании каких-либо библиотек, укажите их в файле
# requirements.txt
#- при выполнении кода не должно возникать ошибок
#- свой проект нужно закинуть в GitHub


class Cars:
    objects = []
    list_ = []
    _id = 0
    body_types = ("седан", "универсал", "купе", "хэтчбек", "минивен", "внедорожник", "пикап")


    def __init__(self, brand, model, year, engine_volume, color,body_type, mileage, price):
        self.id = Cars._id
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.color = color
        if body_type in Cars.body_types:
            self.body_type = body_type
        else:
            raise Exception("Cars 'body_type' is not valid")
        self.mileage = mileage
        self.price = price
        Cars.objects.append(self)
        Cars._id += 1
        Cars.list_.append({"id": self.id, "brand": self.brand, "model": self.model, "year": self.year, "engine_volume": self.engine_volume, "color": self.color, "body_type": body_type, "mileage": self.mileage, "price": self.price})
        

    def get_info(self):
        return f"моя машина марки: {self.brand},\n id: {self.id},\nмодель:{self.model},\nгод выпуска: {self.year},\nобъем двигателя: {self.engine_volume},\nцвет машины: {self.color},\nтип кузова: {self.body_type},\nпробег машины: {self.mileage},\nцена: {self.price}"

# a1 = Cars("Lexus", "RX470", 2018, 13.2, "Black", "внедорожник", 7200, 45000.00)
# a2 = Cars("Toyota", "Raum", 2015, 8.5, "Red", "хэтчбек", 13300, 6500.00)
# print(a1.get_info())
# print(a2.get_info())
# Cars.objects.append(a1)
# Cars.objects.append(a2)















        
        