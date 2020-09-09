#-------------------------------------------------
#  S.O.L.I.D Principles
#    - Definition
#    - Design Principles -vs- Design Patterns
#    - Application & Entities
#-------------------------------------------------


# Add notes & experimentation codes here


#-------------------------------------------------
#  Single Responsibility Principle
#    - Definition
#    - Applies To (Entities)
#-------------------------------------------------


# Add notes & experimentation codes here


#-------------------------------------------------
#  PRACTICAL EXAMPLE
#
#  We want to be able to manage a list of products (create & delete) and
#  add the ones we are interested in to a cart so we can set quantity for
#  each product and get the total price before checking out
#-------------------------------------------------

class Store:
    def __init__(self):
        self.data = {}

    def add(self, params):
        _id = params['id']
        self.data[_id] = params

    def remove(self, _id):
        del self.data[_id]

class Products(Store):
    def create(self, params):
        self.add(params)

    def delete(self, _id):
        self.remove(_id)

class Cart(Store):
    def get_total_price(self):
        return sum([product['price'] for product in self.data.values()])

# Admin

products = Products()

products.create({ 'id': 1, 'name': 'Headset', 'price': 100})
products.create({ 'id': 2, 'name': 'Printer', 'price': 200})
products.create({ 'id': 3, 'name': 'Indomie Pack', 'price': 1500})

# Customer 1

print('\nAll Products 1\n')
print(products.data)

user_cart_1 = Cart()

user_cart_1.add(products.data[1])
user_cart_1.add(products.data[3])

print('\nUser Cart Products 1\n')
print(user_cart_1.data)

print('\nUser Cart Total 1\n')
print(user_cart_1.get_total_price())

# Customer 2

print('\nAll Products 2\n')
print(products.data)

user_cart_2 = Cart()

user_cart_2.add(products.data[1])
user_cart_2.add(products.data[2])

print('\nUser Cart Products 2\n')
print(user_cart_2.data)

print('\nUser Cart Total 2\n')
print(user_cart_2.get_total_price())

print('\nUser Cart Delete 2\n')
user_cart_2.remove(2)

print('\nUser Cart Total 2\n')
print(user_cart_2.get_total_price())