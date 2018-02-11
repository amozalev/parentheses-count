class Discount(object):
    def __init__(self, name, time_start, time_end, **kwargs):
        self.time_start = time_start
        self.time_end = time_end
        self.name = name
        self.discounts = kwargs
        self.discount_single_product = 0
        self.discount_brand = 0
        self.discount_group = 0
        self.discount_client = 0
        print(f'Сделали скидку "{self.name}" на {self.discount}% в период c {self.time_start} до {self.time_end}.')

    @property
    def discount(self):
        for key, value in self.discounts.items():
            setattr(self, key, value)
        return self.discount_single_product + self.discount_brand + self.discount_group + self.discount_client

    def __str__(self):
        return f'{self.name}: {self.discount_single_product}, {self.discount_brand}, {self.discount_group}, {self.discount_client}'


class Category(object):
    def __init__(self, name):
        self.name = name


class Product():
    def __init__(self, name, price, Category):
        self.name = name
        self.price = float(price)
        self.category = Category
        self.discount = 0

    def set_discount(self, Discount):
        self.discount = Discount.discount
        self.price = float(self.price - self.discount * self.price / 100)
        return self.discount

    def __str__(self):
        return f'Товар: {self.name}, Категория: {self.category.name}, Цена: {self.price} руб., Скидка: {self.discount}%'


def main():
    food = Category('Еда')
    apple = Product('яблоко Гольден', 100, food)
    print(apple)
    discount = Discount('Сезонная скидка на яблоки',
                        '2018-09-01',
                        '2018-10-01',
                        discount_single_product=10,
                        discount_group=15)
    apple.set_discount(discount)
    print(apple)


if __name__ == '__main__':
    main()
