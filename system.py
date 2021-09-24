
from menu import Menu
from order import Order
from calculate import Calculate

from system_state import SystemState, OrderState

class System:
  def __init__(_self):
    _self.menu = Menu()
    _self.order = Order()
    _self.systemState = SystemState.START
    _self.orderState = OrderState.NO

  def main(_self):

    while _self.systemState == SystemState.START:

      _self.menu.printMenuList()
      menuInput = int(input('\nEnter your selection\n'))

      if menuInput not in range(1,3):
        print('\nInvalid Selection. Reselect')
        continue

      if menuInput == 2:
        _self.systemState = SystemState.END

        if _self.orderState == OrderState.NO:
          print('Order State %s' % (_self.orderState))
          break

        calculate = Calculate(_self.order.getOrderList())
        calculate.printReceipt();
        break
        

      _self.menu.printProductList();
      orderInput = input('\nEnter your order(Eg. 1 2 4):\n')  
      _self.order.addOrder(orderInput)
      _self.orderState = OrderState.YES
      

    

#Start from here
system = System()
system.main()



      
