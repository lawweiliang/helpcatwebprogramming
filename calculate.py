
class Calculate:
  def __init__(_self, _orderObjectList):
    _self.orderObjectList = _orderObjectList.copy()


  def total(_self):
    total = 0
    for food in _self.orderObjectList:
        total += food.totalCost;
    
    return total;


  def printReceipt(_self):
    print('\n\n\n')
    print('Receipt:')
    print('========')

    for index ,food in enumerate(_self.orderObjectList):
      if food.quantity != 0:
        print('%s. %s %s RM %s' % (index+1, food.name, food.quantity, food.totalCost))

    print('========')
    print('Total: RM %s' % (_self.total()))



""" from order import Order
order = Order();
order.addOrder('1 3 2')
order.addOrder('1 3 4')
orderList = order.getOrderList();

for food in order.getOrderList():
  print('id:%s, name:%s, price:%s, quantity:%s' % (food.id, food.name, food.price, food.quantity))


calculate = Calculate(orderList)
calculate.printReceipt(); """