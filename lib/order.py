class Order:
    def __init__(self):
        self.basket = []
        self.order_menu_items = []

    def choose_menu(self, menu):
        self.order_menu_items = menu.menu_items

    def add_to_basket(self, dish_to_add):
        for menu_item in self.order_menu_items:
            if menu_item.item == dish_to_add:
                self.basket.append(menu_item)

    def view_current_basket(self):
        final_menu_string = ''
        for menu_item in self.basket:
            item = menu_item.item
            price = "{:.2f}".format(menu_item.price)
            final_menu_string += f'{item} : £{price}, '
        return final_menu_string[:-2]

    def view_reciept(self):
        bill_total = 0
        for menu_item in self.basket:
            bill_total += menu_item.price
        return self.view_current_basket() + f' | BILL TOTAL: £{bill_total:.2f}'
        
