class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def get_by_letter(self, first_letter):
        list_starting_with_the_letter = [element for element in self.products if element[0] == first_letter]
        return list_starting_with_the_letter
    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        sorted_items = sorted(self.products)
        for product in sorted_items:
            result += f"{product}\n"
        return result

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)




