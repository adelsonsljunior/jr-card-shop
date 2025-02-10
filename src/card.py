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
        return (
            f"ID: {self.id}\n"
            f"Jogo: {self.game}\n"
            f"Carta: {self.name}\n"
            f"Raridade: {self.rarity}\n"
            f"Preço Unitário: R$ {self.price:.2f}\n"
            f"Unidades em Estoque: {self.stock}\n"
            f"Unidades Vendidas: {self.sold}\n"
        )
