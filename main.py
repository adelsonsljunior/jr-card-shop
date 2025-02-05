class Card:

    def __init__(self, id, name, game, rarity, price, stock, sold):
        self.id = id
        self.game = game
        self.name = name
        self.rarity = rarity
        self.price = price
        self.stock = stock
        self.sold = sold

    def __str__(self):
        return f"id: {self.id}, game: {self.game}, name: {self.name}, rarity: {self.rarity}, price: {self.price}, stock: {self.stock}, sold: {self.sold}"


games = {1: "Yu-Gi-Oh", 2: "Pokémon", 3: "Digimon"}

rarities = {1: "Common", 2: "Rare", 3: "Super Rare", 4: "Ultra Rare"}

cards = [
    Card(1, "Red-Eyes Black Dragon", games[1], rarities[4], 100.00, 10, 0),
    Card(2, "Blue-Eyes White Dragon", games[1], rarities[4], 200.00, 5, 0),
    Card(3, "Dark Magician", games[1], rarities[4], 150.00, 7, 0),
    Card(4, "Garchomp", games[2], rarities[4], 100.00, 10, 0),
    Card(5, "Tyranitar", games[2], rarities[4], 200.00, 5, 0),
    Card(6, "Mewtwo", games[2], rarities[4], 500.00, 7, 0),
    Card(7, "Greymon", games[3], rarities[4], 100.00, 10, 0),
    Card(8, "MetalGreymon", games[3], rarities[4], 200.00, 5, 0),
    Card(9, "WarGreymon", games[3], rarities[4], 300.00, 7, 0),
]

def display_games():
    print("\n" + "=" * 15)
    for key, value in games.items():
        print(f"{key} - {value}")
    print("=" * 15 + "\n")

def register_card():

    game = input("Digite o name do game: ")
    name = input("Digite o name da carta: ")
    rarity = input("Digite a rarity da carta: ")
    price = float(input("Digite o preço da carta: "))
    stock = int(input("Digite a quantidade em estoque: "))

    card = Card(name, game, rarity, price, stock)

    cards.append(card)


def list_cards():
    print("\n" + "=" * 100)
    for card in cards:
        print(card)
    print("=" * 100 + "\n")


def list_cards_by_game():
    
    display_games()
    game = int(input("Digite o jogo desejado: "))

    print("\n" + "=" * 100)
    for card in cards:
        if card.game == games[game]:
            print(card)
    print("=" * 100 + "\n")


def list_cards_by_rarity(rarity):
    print("Hey Marceline")


def find_card_by_id(id):
    print("Hey Marceline")


def menu():
    opt = 0

    while opt != 6:
        print("\n" + "=" * 20)
        print("1 - Cadastrar Carta")
        print("2 - Listar Cartas")
        print("3 - Listar Cartas por Jogo")
        print("0 - Sair")
        print("=" * 20 + "\n")

        opt = int(input("Digite a opção desejada: "))

        match opt:
            case 1:
                register_card()
            case 2:
                list_cards()
            case 3:
                list_cards_by_game()
            case _:
                print("Opção inválida")

        if opt == 0:
            break


if __name__ == "__main__":
    menu()
