from lib.menu_item import *
import pytest

def test_init_with_item_and_price():
    menu_item = MenuItem('Item', 10)
    assert menu_item.item == 'Item'
    assert menu_item.price == 10

def test_type_error_raised_if_item_not_string():
    with pytest.raises(TypeError) as e:
        menu_item = MenuItem(10, 10)
    error_message = str(e.value)
    assert error_message == 'Item must be a string.'

def test_type_error_raise_if_price_not_type_float():
    with pytest.raises(TypeError) as e:
        menu_item = MenuItem('Item', "chips")
    error_message = str(e.value)
    assert error_message == 'Price must be an integer or float.'

    