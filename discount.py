class Discount(object):
    def __init__(self, time_start, time_end, **kwargs):
        self.time_start = time_start
        self.time_end = time_end
        self.name = kwargs['name']
        # self.discount_single_product =


# class DiscountSingleProduct():
#     pass
#
#
# class DiscountBrand():
#     pass
#
#
# class DiscountProductsGroup():
#     pass
#
#
# class DiscountClient():
#     pass
#

class Category(object):
    def __init__(self, name):
        self.name = name


class Product():
    def __init__(self, name, price, Category, Discount):
        self.name = name
        self.price = price
        self.category = Category
        self.discount = Discount

    def __str__(self):
        return f'{self.name}, {self.price}, {self.category.name}, {self.discount}'


def main():
    food = Category('Еда')
    apple = Product('яблоко', 100, food, 0)
    print(apple)


if __name__ == '__main__':
    main()
