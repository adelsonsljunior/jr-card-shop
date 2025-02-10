import repository
from card import Card
from dictionaries import games, rarities


def display_games():
    print("\n" + "=" * 15)
    for key, value in games.items():
        print(f"{key} - {value}")
    print("=" * 15 + "\n")


def display_rarities():
    print("\n" + "=" * 15)
    for key, value in rarities.items():
        print(f"{key} - {value}")
    print("=" * 15 + "\n")


def register_card():

    display_games()
    game = int(input("Digite o jogo da carta: "))
    name = input("Digite o name da carta: ")
    display_rarities()
    rarity = int(input("Digite a rarity da carta: "))
    price = float(input("Digite o preço da carta: "))
    stock = int(input("Digite a quantidade em estoque: "))

    # Gerar um id para a carta
    card_id = len(cards) + 1

    card = Card(card_id, name, games[game], rarities[rarity], price, stock)

    cards.append(card)

    print("\n[INFO] - Carta cadastrada com sucesso")


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
    print("=" * 100)


def list_cards_by_rarity():

    display_rarities()
    rarity = int(input("Digite a raridade desejada: "))

    print("\n" + "=" * 100)
    for card in cards:
        if card.rarity == rarities[rarity]:
            print("\n" + "=" * 100)
            print(card)
            print("=" * 100)


def find_card_by_id():

    id = int(input("Digite o id da carta: "))
    for card in cards:
        if card.id == id:
            print("\n" + "=" * 100)
            print(card)
            print("=" * 100 + "\n")


def sell_cards():
    print("Hey Marceline")


def stock_replacement():
    print("Hey Marceline")


def sales_report():
    print("Hey Marceline")


def menu():
    opt = 0

    while opt != 6:
        print("\n" + "=" * 20)
        print("1 - Cadastrar Carta")
        print("2 - Listar Cartas")
        print("3 - Listar Cartas por Jogo")
        print("4 - Listar Cartas por Raridade")
        print("5 - Buscar Carta por id")
        print("6 - Vender Cartas")
        print("7 - Reposição de Estoque")
        print("8 - Relatório de Vendas")
        print("9 - Sair")
        print("=" * 20 + "\n")

        opt = int(input("Digite a opção desejada: "))

        match opt:
            case 1:
                register_card()
            case 2:
                list_cards()
            case 3:
                list_cards_by_game()
            case 4:
                list_cards_by_rarity()
            case 5:
                find_card_by_id()
            case 9:
                print("Saindo...")
                break
            case _:
                print("Opção inválida")


if __name__ == "__main__":
    menu()
