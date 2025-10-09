class Flower:
    def __init__(self, name, color, length, lifetime, price):
        self.name = name
        self.color = color
        self.length = length
        self.lifetime = lifetime
        self.price = price


class Poppy(Flower):

    def __init__(self, length, price):
        super().__init__('Poppy', 'red', length, 15, price)


class Cornflower(Flower):

    def __init__(self, length, price):
        super().__init__('Cornflower', 'blue', length, 10, price)


class Sunflower(Flower):

    def __init__(self, length, price):
        super().__init__('Sunflower', 'yellow', length, 30, price)


class Rose(Flower):

    def __init__(self, length, price):
        super().__init__('Rose', 'red', length, 10, price)


class Bouquet:

    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def bouquet_cost(self):
        return sum(flower.price for flower in self.flowers)

    def average_lifetime(self):
        return round(sum(flower.lifetime for flower in self.flowers) / len(self.flowers), 2)

    def sort_flowers_by_lifetime(self):
        self.flowers.sort(key=lambda x: x.lifetime, reverse=True)

    def sort_flowers_by_price(self):
        self.flowers.sort(key=lambda x: x.price, reverse=True)

    def sort_flowers_by_length(self):
        self.flowers.sort(key=lambda x: x.length, reverse=True)

    def find_flowers_by_color(self, color):
        result = []
        for flower in self.flowers:
            if flower.color == color:
                result.append(flower)
        return result


poppy1 = Poppy(50, 100)
cornflower1 = Cornflower(20, 20)
sunflower1 = Sunflower(100, 10)
rose1 = Rose(30, 200)


bouquet1 = Bouquet()
bouquet1.add_flower(poppy1)
bouquet1.add_flower(cornflower1)
bouquet1.add_flower(sunflower1)
bouquet1.add_flower(rose1)


print(f"Bouquet cost: {bouquet1.bouquet_cost()}")
print(f"Average lifetime: {bouquet1.average_lifetime()}")

bouquet1.sort_flowers_by_lifetime()
print('Flowers sorted by lifetime:')
for flower in bouquet1.flowers:
    print(f'{flower.name}: {flower.lifetime}')

bouquet1.sort_flowers_by_price()
print('Flowers sorted by price:')
for flower in bouquet1.flowers:
    print(f'{flower.name}: {flower.price}')
    
bouquet1.sort_flowers_by_length()
print('Flowers sorted by length:')
for flower in bouquet1.flowers:
    print(f'{flower.name}: {flower.length}')

flowers_found = bouquet1.find_flowers_by_color(color='red')
print('Flowers found by color:')
for flower in flowers_found:
    print(f'{flower.name}: {flower.color}')
