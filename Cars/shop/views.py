from abstract.utils import get_obj_or_404
from .models import Cars, Comment
from .serializers import CarsSerializer
from account.models import User


def car_create():
    brand = str(input("Введите марку: "))
    model= str(input("Введите модель: "))
    year = int(input("Введите год выпуска: "))
    engine_volume = round(float(input("Введите объем двигателя: ")), 1)
    color = str(input("Введите цвет машины: "))
    body_type = input("Введите тип кузова: ")
    mileage = int(input("Введите пробег машины: "))
    price = round(float(input("Введите цену машины: ")), 2)


    Cars(brand, model, year, engine_volume, color,body_type, mileage, price)
    return "Продукт успешно создан"

def car_listing():
    serializer = CarsSerializer()
    car = serializer.serialize_queryset()
    return car


def car_retrieve(p_id):
    car = get_obj_or_404(Cars, "id", int(p_id))
    serializer = CarsSerializer()
    return serializer.serialize_obj(car)
    
def car_delete(p_id):
    car = get_obj_or_404(Cars, "id", int(p_id))
    Cars.objects.remove(car)
    return "Продукт успешно удален"

def car_update(p_id):
    car = get_obj_or_404(Cars, "id", int(p_id))
    field = input("Введите поле для изменения: ")
    if field in dir(car):
        print(f"old value: {getattr(car, field)}")
        value = input(f"{field} = ")
        setattr(car, field, value)
    else:
        raise Exception(f"Поля {field} нет в продукте")
    return car_retrieve(p_id)


def create_comment():
    email = input("Введите email: ")
    user = get_obj_or_404(User, "email", email)
    print("Выберите машину: ")
    for p in Cars.objects:
        print(p.title)
    brand = input("============================\n")
    car = get_obj_or_404(Cars, " brand", brand)
    body = input("Введите комментарии: ")
    Comment(user, car, body)
    return "Комментарий успешно создан"


u = User('Zhiide', 'Zhiide', 'hello')
u.register('12345', '12345')
u.login('12345')
lexus = Cars("Lexus", "RX470", 2018, 13.2, "Black", "внедорожник", 7200, 45000.00)
Comment(u, lexus, "Python21 cool")


    


