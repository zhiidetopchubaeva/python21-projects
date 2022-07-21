from unicodedata import category
from account.models import MyUser
from .models import Product, Comment
from .serializers import ProductSerializer

def create_product():
    category = input("Введите категорию: ")
    title = input("Введите название: ")
    price = float(input("Введите цену: "))
    description = input("Введите описание: \n")
    Product.create(category=category, title=title, price=price, description=description)
    return "Продукт успешно создан"

def product_list():
    return ProductSerializer().serialize_queryset()

def create_comment(p_id):
    from datetime import datetime
    username = input("Введите юзернейм: ")
    user = MyUser.get(username=username)
    product = Product.get_by_id(p_id)
    body = input("Введите комментарий: \n")
    created_at = datetime.now()
    Comment.create(user=user, product=product, body=body, created_at=created_at)
    return "Комментарий успешно создан"
    