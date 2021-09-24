
class Food:
  def __init__(self, _id, _name, _price, _quantity):
    self.id = _id
    self.name = _name
    self.price = _price
    self.quantity = _quantity
    self.totalCost = _price * _quantity

  def __str__(self):
    return "Id:%s, Name: %s, Price: %s, Quantity: %s" % (self.id, self.name, self.price, self.quantity)


""" food1 = Food(1,'rice', 30, 2)
food1.price += 1
print('Food Name: ' + food1.name)
print('Food price: ' + str(food1.price))
print('Food quantity: ' + str(food1.quantity))
print(food1)

print(Food(1,'rice', 30, 2)); """

