from food_stock import FoodStock

class Order:
  def __init__(_self):
    foodStock = FoodStock()
    _self.foodStock = foodStock.getFoodList()

    _self.orderList = [0] * len(_self.foodStock)

  # orderList is string , eg 1, 2, 3
  def addOrder(_self, _orderList):
    order = _orderList.split(' ')

    for orderNum in order:
      if int(orderNum) in range(0, len(_self.foodStock)+1):
        _self.orderList[int(orderNum)-1] += 1

  ### return orderlist with food details
  def getOrderList(_self):
    foodOrderList = _self.foodStock.copy()

    for index, orderQuantity in enumerate(_self.orderList):
      foodOrderList[index].quantity = orderQuantity;
      foodOrderList[index].totalCost = foodOrderList[index].quantity * foodOrderList[index].price;

    return foodOrderList;




# order = Order()
# # order.addOrder('1 3 5')
# order.addOrder('1 3 2')
# order.addOrder('1 3 4')
# # print (order.getOrderList())

# for food in order.getOrderList():
#   print('id:%s, name:%s, price:%s, quantity:%s' % (food.id, food.name, food.price, food.quantity))



  

