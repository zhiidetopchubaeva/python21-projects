
from shop.models import Product, Category
from shop.views import product_create, product_detail, product_list, product_update

cat = Category("phones")
Category("dyson")
Category("food")

obj1 = Product("iphone 10", 234, "...", 3, cat)
obj2 = Product("iphone 11", 200, "...", 10, cat)
obj3 = Product("iphone 13", 239, "...", 5, cat)


from pprint import pprint # для вывода в строку
pprint(product_create())
pprint(product_list())
id_ = input("Введите продукт для обновления: ")
pprint(product_update(id_))
