# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class System

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

dishes, prices, see_all_dishes_and_prices, 

order a dish

reciept, itemised, grand total

menu.show_menu() => show whole menu, with prices
my_order.choose_dish(menu, menu_item) 
my_reciept = Recipt()

_Also design the interface of each class in more detail._

```python
class Order:
    #User-facing properties 
    #basket: a list of instances of menu items
    def __init__(self, menu):
        #initialised with an instance of a menu
        pass
        #No code here yet


    def add_to_basket(self, dish_to_add)
        #Parameters: name of the dish to add to the basket, dish_to_add a string
        #Side-effects: Adds dish to basket list
        #Returns nothing

class Menu:
    #public properties: a menu dictionary
    def __init__(self, *menu_item):
        #Initialised with many menu_item objects key: item, value: price

    def show_menu(self):
        #parmeters: none
        #returns whole menu with items and prices

class MenuItem:
    #Public properties: an item value as a string and a price value as float
    def __init__(self, item, price)


class Reciept:
    def __init__(self, order)
    #Initialised with an instance of an order.

    def show_reciept(self)
    #No parameters
    #Returns an itemised reciept for the order object and a grand total

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
"""
Given a menu item, this menu item is added to menu and appears in menu list
"""
menu_item = MenuItem('Chips', 1.50)
my_menu = Menu(menu_item)
my_menu.menu # => [menu_item]

"""
Given two menu item objects, they appear in the menu list
"""
menu_item = MenuItem('Chips', 1.50)
menu_item2 = MenuItem('Burger', 10.00)
my_menu = Menu(menu_item, menu_item2)
my_menu.menu # => [{menu_item, menu_item2]

"""
Given two menu item objects added to Menu, show_menu dispays nice string of items and prices
"""

menu_item = MenuItem('Chips', 1.50)
menu_item2 = MenuItem('Burger', 10.00)
my_menu = Menu(menu_item, menu_item2)
my_menu.show_menu() #=> Chips : £1.50 , Burger : £10.00

"""
Given a menu_item, a menu and an Order
When we add a dish to the basket.
the dish is then included in the order basket
"""
menu_item = MenuItem('Chips', 1.50)
my_menu = Menu(menu_item)
order = Order(my_menu)
order.add_dish_to_basket('Chips')
order.basket #=> [menu_item]

"""
Given an order item
When the order is called by a reciept object
the order items are displayed and a grand total is given
"""
menu_item = MenuItem('Chips', 1.50)
menu_item2 = MenuItem('Burger', 10.00)
my_menu = Menu(menu_item, menu_item2)
order = Order(my_menu)
order.add_dish_to_basket('Chips')
order.add_dish_to_basket('Burger')
receipt = Reciept(order)
reciept.show_reciept() # => 'Chips : £1.50, Burger : £10.00, Total : £11.50'


## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

#MENU ITEM UNIT TESTS ---------------------------------------------------
"""
Given a menu item object
that menu item is stored as a key value pair of item: key
"""
menu_item = MenuItem('Chips', 1.50)
menu_item.item #=> 'Chips'
menu_item.price #=> 1.50

"""
Raise error if item is not string type
"""
menu_item = MenuItem(0, 1.50)# => Raise exception 'Item must be of type string'

"""
Raise error if price is not float type
"""
menu_item = MenuItem('Chips', 'Burger') #=> Raise exception 'Price must be a float'

#MENU UNIT TESTS -------------------------------------------------------
"""
Given a menu initialised with a single menu_item object, said menu_item is
in menu_items
"""
menu_item = Mock()
menu = Menu(menu_item) #=> menu_item will need to be a Mock menu item
menu.menu_items # => [menu_item]

"""
Given a menu initiailsed with multiple menu_items
they are included in the menu_items list
"""
menu_item1 = Mock()
menu_item2 = Mock()
menu_item3 = Mock()
menu = Menu(menu_item1, menu_item2, meun_item3)
menu.menu_items # => [menu_item1, menu_item2, menu_item3]

"""
Test if Menu show menu dispays item and price string
"""
menu_item1 = Mock()
menu_item1.item.return_value = 'Chips'
menu_item1.price.return_value = 1.5
menu_item2= Mock()
menu_item2.item.return_value = 'Burger'
menu_item2.price.return_value = 10
menu_item3= Mock()
menu_item3.item.return_value = 'Kebab'
menu_item3.price.return_value = 11
menu = Menu(menu_item1, menu_item2, menu_item3)
menu.show_menu # Chips : £1.50 , Burger : £10.00, Kebab : £11.00

#Order Class Unit tests

"""
Test if new Order is initialised with a menu
"""
menu_item = Mock()    #NEED TO FIGURE OUT HOW TO MOCK CLASS WITHIN A CLASS
my_menu = Menu(menu_item) # MOCKS required for menu_item and menu
my_order = Order(my_menu)
my_order.menu = my_menu

"""
Test if a order object is init with an empty basket list
"""
menu_item = Mock()
my_menu = Menu(menu_item) #More mocks required
my_order = Order(my_menu)
my_order.basket # => []

"""
Test if a menu item is added to an the order basket
"""
menu_item = Mock()
menu_item.item.return_value = "Chips"
my_menu = Menu(menu_items)
my_order = Order(my_menu)
my_order.add_to_basket('Chips')
my_order.basket #=> [menu_item]

"""
Test if a menu item is added to an the order basket
"""
menu_item1 = Mock()
menu_item2 = Mock()
menu_item1.item.return_value = "Chips"
menu_item2.item.return_value = "Burger"
my_menu = Menu(menu_item1, menu_item2)
my_order = Order(my_menu)
my_order.add_to_basket('Chips')
my_order.basket #=> [menu_item]


_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
