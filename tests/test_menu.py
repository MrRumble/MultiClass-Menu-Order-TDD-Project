from lib.menu import *
from unittest.mock import Mock

def test_menu_init_with_empty_list():
    menu = Menu()
    assert menu.menu_items == []

def test_add_menu_items_to_menu_list():
    fake_menu_item1 = Mock()
    fake_menu_item2 = Mock()
    fake_menu_item3 = Mock()
    menu = Menu()
    menu.add_to_menu(fake_menu_item1, fake_menu_item2, fake_menu_item3)
    assert menu.menu_items == [fake_menu_item1, fake_menu_item2, fake_menu_item3]

def test_show_menu_displays_one_item_menu():
    menu_item1 = Mock()
    menu_item1.item.return_value = 'Chips'
    menu_item1.price.return_value = 1.5
    menu = Menu()
    menu.add_to_menu(menu_item1)
    assert menu.show_menu() == 'Chips : £1.50'

def test_show_menu_displays_one_item_menu_format_price():
    menu_item1 = Mock()
    menu_item1.item.return_value = 'Burger'
    menu_item1.price.return_value = 10
    menu = Menu()
    menu.add_to_menu(menu_item1)
    assert menu.show_menu() == 'Burger : £10.00'

def test_if_show_menu_displays_item_and_price_as_string():
    menu_item1 = Mock()
    menu_item1.item.return_value = 'Chips'
    menu_item1.price.return_value = 1.5
    menu_item2= Mock()
    menu_item2.item.return_value = 'Burger'
    menu_item2.price.return_value = 10
    menu_item3= Mock()
    menu_item3.item.return_value = 'Kebab'
    menu_item3.price.return_value = 11
    menu = Menu()
    menu.add_to_menu(menu_item1, menu_item2, menu_item3)
    result = menu.show_menu()
    assert result == 'Chips : £1.50, Burger : £10.00, Kebab : £11.00'


