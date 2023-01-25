# *args allows multiple positional arguments
# def add(*args):
#     no = 0
#     for n in args:
#         no += n
#     print(no)
#
#
# add(10, 5, 15, 25)


# **kwargs allows multiple keywords arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    #     n += kwargs["add"]
    #     n += kwargs["multiply"]
    #     print(n)




calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        # self.model = kwargs["model"]
        """In order to avoid errors in console when a keyword argument is not provided, we use the Get method 
        so its provides NONE if it doesn't exist"""
        self.model = kwargs.get("model")

my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)