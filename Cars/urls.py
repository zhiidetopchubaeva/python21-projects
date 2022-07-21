from shop.views import *
from account.views import *

urlpatterns = [
    ('cars/', car_listing),
    ('car-create/', car_create),
    ('car-retrieve/id', car_retrieve),
    ('car-update/id', car_update),
    ('car-delete/id', car_delete),
    ('comment-create/', create_comment)
]
