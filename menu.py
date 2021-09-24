from food_stock import FoodStock

class Menu:
  def getMenuList(self):
   return ['Buy Product', 'Quit']

  def printMenuList(self):
    menuList = self.getMenuList()
    
    print('\n\n')
    print('Main Menu')
    for menuItem in menuList:
      print(str(menuList.index(menuItem)+1) + '.' + menuItem)


  def printProductList(_self):
    foodStock = FoodStock()
    foodList = foodStock.getFoodList();

    print('\n\n')
    print('Food Menu')
    print('=========')
    for index, food in enumerate(foodList):
      print('%s. name: %s, price: %s, quantity: %s' % (index+1, food.name, food.price, food.quantity))


# menu = Menu()
# menu.printMenuList()
# menu.printProductList()