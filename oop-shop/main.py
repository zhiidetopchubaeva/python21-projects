from nis import cat
from shop.models import Product, Category
from shop.serializers import ProductSerializer

cat = Category("phones")
obj1 = Product("iphone 10", 234, "...", 3, cat)
obj2 = Product("iphone 11", 200, "...", 10, cat)
obj3 = Product("iphone 13", 239, "...", 5, cat)

res = ProductSerializer().serialize_queryset([obj1, obj2, obj3])
from pprint import pprint # для вывода в строку
pprint(res)