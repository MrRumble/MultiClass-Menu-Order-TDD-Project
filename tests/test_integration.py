from lib.menu_item import *
from lib.menu import *
from lib.order import *

def test_menu_item_is_added_to_order_basket():
    menu_item = MenuItem('Chips', 1.50)
    menu = Menu()
    menu.add_to_menu(menu_item)
    order = Order()
    order.choose_menu(menu)
    order.add_to_basket('Chips')
    assert order.basket == [menu_item]

def test_choose_menu_adds_menu_items_to_order_menu_items():
    chips = MenuItem('Chips', 1.50)
    burger = MenuItem('Burger', 10)
    my_menu = Menu()
    my_menu.add_to_menu(chips, burger)
    my_order = Order()
    my_order.choose_menu(my_menu)
    assert my_order.order_menu_items == [chips, burger]

def test_menu_items_added_to_order_basket():
    menu_item1 = MenuItem('Chips', 1.5)
    menu_item2 = MenuItem('Burger', 10)
    menu_item3 = MenuItem('Fish', 20)
    menu = Menu()
    menu.add_to_menu(menu_item1, menu_item2, menu_item3)
    my_order = Order()
    my_order.choose_menu(menu)
    my_order.add_to_basket('Chips')
    my_order.add_to_basket('Burger')
    my_order.add_to_basket('Fish')
    assert my_order.basket == [menu_item1, menu_item2, menu_item3]

def test_view_current_basket_three_items():
    menu_item1 = MenuItem('Chips', 1.5)
    menu_item2 = MenuItem('Burger', 10)
    menu_item3 = MenuItem('Fish', 20)
    menu = Menu()
    menu.add_to_menu(menu_item1, menu_item2, menu_item3)
    my_order = Order()
    my_order.choose_menu(menu)
    my_order.add_to_basket('Chips')
    my_order.add_to_basket('Burger')
    my_order.add_to_basket('Fish')
    assert my_order.view_current_basket() == 'Chips : £1.50, Burger : £10.00, Fish : £20.00'

def test_view_basket_one_item():
    menu_item1 = MenuItem('Chips', 1.5)
    menu = Menu()
    menu.add_to_menu(menu_item1)
    order = Order()
    order.choose_menu(menu)
    order.add_to_basket('Chips')
    assert order.view_current_basket() == 'Chips : £1.50'

def test_one_item_on_order_show_reciept_shows_item_and_total():
    chips = MenuItem('Chips', 1.5)
    chip_shop = Menu()
    chip_shop.add_to_menu(chips)
    customer = Order()
    customer.choose_menu(chip_shop)
    customer.add_to_basket('Chips')
    assert customer.view_reciept() == "Chips : £1.50 | BILL TOTAL: £1.50"

def test_view_current_basket_three_items():
    menu_item1 = MenuItem('Chips', 1.5)
    menu_item2 = MenuItem('Burger', 10)
    menu_item3 = MenuItem('Fish', 20)
    menu = Menu()
    menu.add_to_menu(menu_item1, menu_item2, menu_item3)
    my_order = Order()
    my_order.choose_menu(menu)
    my_order.add_to_basket('Chips')
    my_order.add_to_basket('Burger')
    my_order.add_to_basket('Fish')
    assert my_order.view_current_basket() == 'Chips : £1.50, Burger : £10.00, Fish : £20.00'


