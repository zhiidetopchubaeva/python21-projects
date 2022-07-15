import permissions

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


    @property
    def comments(self):
        return [c for c in Comment.objects if c.car == self]


class Comment:
    objects = []

    def __init__(self, user, car, body):
        permissions.login_required(user)
        from datetime import datetime
        self.user = user
        self.car = car
        self.body = body
        self.created_at = datetime.now()
        Comment.objects.append(self)
    
    def __str__(self):
        return f"{self.user.email} - [{self.created_at}] - {self.body}"

