from food import Food

class FoodStock:
  def __init__(_self):
    defaultFoodStockList = _self._defaultFoodStockList();
    _self.foodList = []
    for food in defaultFoodStockList:
      _self.foodList.append(Food(food['id'],food['name'], food['price'], food['quantity']))

  def getFood(_self, _index):
    return _self.foodList[_index]

  def getFoodList(_self):
    return _self.foodList

  def updateFoodQuantity(_self, _index, _quantity):
    _self.foodList[_index].quantity = _quantity

  def updateFoodPrice(_self, _index, _price):
    _self.foodList[_index].price = _price;

  def _defaultFoodStockList(_self):
    return [
    {'id':1,'name':'Nasi Lemak', 'price':2.5, 'quantity':5},
    {'id':2,'name':'Milo Ais', 'price':1.5, 'quantity':10},
    {'id':3,'name':'Mee Kuteow', 'price':6, 'quantity':20},
    {'id':4,'name':'Chicken Chop', 'price':10, 'quantity':30},
    {'id':5,'name':'Coca-Cola', 'price': 3, 'quantity':20},
    ]





# foodStock = FoodStock();

# print(foodStock._defaultFoodStockList());
# print(foodStock.getFoodList())

# foodList = foodStock.getFoodList();
# for food in foodList:
#   print('name: %s, price: %s, quantity: %s' % (food.name, food.price, food.quantity))
