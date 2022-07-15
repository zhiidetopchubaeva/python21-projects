from abstract.utils import get_obj_or_404
from .models import Product, Category, Comment
from .serializers import ProductSerializer, CategorySerializer
from account.models import User

def product_list():
    serializer = ProductSerializer()
    products = serializer.serialize_queryset()
    return products

def product_create():
    title = input("Введите название: ")
    price = input("Введите цену: ")
    desc = input("Введите описание: ")
    quantity = input("Введите количество: ")

    print("Выберите категорию: ")
    for cat in Category.objects:
        print(cat.title)

    cat_title = input("===========================\n")
    category = get_obj_or_404(Category, "title", cat_title)

    Product(title, price, desc, quantity, category)
    return "Продукт успешно создан"

def product_detail(p_id):
    product = get_obj_or_404(Product, "id", int(p_id))
    serializer = ProductSerializer()
    return serializer.serialize_obj(product)
    
def product_delete(p_id):
    product = get_obj_or_404(Product, "id", int(p_id))
    Product.objects.remove(product)
    return "Продукт успешно удален"

def product_update(p_id):
    product = get_obj_or_404(Product, "id", int(p_id))
    field = input("Введите поле для изменения: ")
    if field in dir(product):
        print(f"old value: {getattr(product, field)}")
        value = input(f"{field} = ")
        setattr(product, field, value)
    else:
        raise Exception(f"Поля {field} нет в продукте")
    return product_detail(p_id)

def category_create():
    title = input('Введите название категории: ')
    Category(title)
    return "Категория была успешно создана"

def create_comment():
    email = input("Введите email: ")
    user = get_obj_or_404(User, "email", email)
    print("Выберите продукт: ")
    for p in Product.objects:
        print(p.title)
    title = input("============================\n")
    product = get_obj_or_404(Product, "title", title)
    body = input("Введите комментарии: ")
    Comment(user, product, body)
    return "Комментарий успешно создан"


u = User('admin', 'admin', 'k')
u.register('12345678', '12345678')
u.login('12345678')
cat = Category('test')
p = Product("hello", 345, "vghjk", 2, cat)
Comment(u, p, "hello world")


    


