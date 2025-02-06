class Card:

    def __init__(self, id, game, name, rarity, price, stock, sold=0):  # sold é opcional
        self.id = id
        self.game = game
        self.name = name
        self.rarity = rarity
        self.price = price
        self.stock = stock
        self.sold = sold  # Valor padrão é 0

    def __str__(self):
        return f"id: {self.id}, game: {self.game}, name: {self.name}, rarity: {self.rarity}, price: {self.price}, stock: {self.stock}, sold: {self.sold}"

