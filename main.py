class Card:

    def __init__(self, id, name, game, rarity, price, stock):
        self.id = id
        self.game = game
        self.name = name
        self.rarity = rarity
        self.price = price
        self.stock = stock
        
    def __str__(self):
        return f"id: {self.id}, game: {self.game}, name: {self.name}, rarity: {self.rarity}, price: {self.price}, stock: {self.stock}"    

cards = [
    Card(1, "Red-Eyes Black Dragon", "Yu-Gi-Oh", "Ultra Rare", 100.00, 10),
    Card(2, "Blue-Eyes White Dragon", "Yu-Gi-Oh", "Ultra Rare", 200.00, 5),
    Card(3, "Dark Magician", "Yu-Gi-Oh", "Ultra Rare", 150.00, 7),
    Card(4, "Gandora the Dragon of Destruction", "Yu-Gi-Oh", "Ultra Rare", 300.00, 3),
    Card(5, "Garchomp", "Pokémon", "Ultra Rare", 100.00, 10),
    Card(6, "Tyranitar", "Pokémon", "Ultra Rare", 200.00, 5),
    Card(7, "Mewtwo", "Pokémon", "Ultra Rare", 500.00, 7),
    Card(8, "Dragonite", "Pokémon", "Ultra Rare", 300.00, 3),
    Card(9, "Salamance", "Pokémon", "Ultra Rare", 200.00, 10),
]



def register_card():

    game = input("Digite o name do game: ")
    name = input("Digite o name da carta: ")
    rarity = input("Digite a rarity da carta: ")
    price = float(input("Digite o preço da carta: "))
    stock = int(input("Digite a quantidade em estoque: "))
    
    card = Card(name, game, rarity, price, stock)
    
    cards.append(card)
    
def list_cards():
    print("\n" + "="*100)
    for card in cards:
        print(card)
    print("="*100 + "\n")
    
def list_cards_by_game(game):
    
    print("Hey Marceline")

def list_cards_by_rarity(rarity):
    print("Hey Marceline")
    
def find_card_by_id(id):
    print("Hey Marceline")    

def menu():
    opt = 0

    while opt != 6:

        print("1 - Cadastrar Carta")
        print("2 - Listar Cartas")
        print("0 - Sair")

        opt = int(input("Digite a opção desejada: "))
        
        match opt:
            case 1:
                register_card()
            case 2:
                list_cards()
            case _:
                print("Opção inválida")
                    

        if opt == 0:
            break

if __name__ == "__main__":
    menu()