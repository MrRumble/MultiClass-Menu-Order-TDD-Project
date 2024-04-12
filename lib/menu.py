class Menu:
    def __init__(self):
        self.menu_items = []
        
    def add_to_menu(self, *menu_items):
        for item in menu_items:
            self.menu_items.append(item)

    def show_menu(self):
        final_menu_string = ''
        for menu_item in self.menu_items:
            item = menu_item.item()
            price = "{:.2f}".format(menu_item.price())
            final_menu_string += f'{item} : £{price}, '
        return final_menu_string[:-2]
            