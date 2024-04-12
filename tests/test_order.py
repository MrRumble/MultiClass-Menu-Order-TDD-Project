from lib.order import *
from unittest.mock import Mock

def test_order_init_with_empty_basket_and_empty_menu_imtes():
    order = Order()
    assert order.basket == []
    assert order.order_menu_items == []


#NEED TO COME BACK AND UNIT TEST WITH MOCKS