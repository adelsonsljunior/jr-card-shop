import repository
from card import Card
from dictionaries import games, rarities


def display_games():
    print("\n" + "=" * 15)
    print("JOGOS".center(15))
    print("" + "=" * 15)
    for key, value in games.items():
        print(f"{key} - {value}")
    print("=" * 15)


def display_rarities():
    print("=" * 15)
    print("RARIDADES".center(15))
    print("=" * 15)
    for key, value in rarities.items():
        print(f"{key} - {value}")
    print("=" * 15)


def format_card_name(name):

    # Remove espaços extras no início e no final
    name = name.strip()

    # Converte para maiúsculas
    name = name.upper()

    # Substitui múltiplos espaços internos por um único espaço
    name = " ".join(name.split())

    return name


def register_card():

    cards = repository.load_cards()

    display_games()
    game = int(input("Digite o jogo da carta: "))
    name = format_card_name(input("Digite o name da carta: "))
    display_rarities()
    rarity = int(input("Digite a rarity da carta: "))
    price = float(input("Digite o preço da carta: "))
    stock = int(input("Digite a quantidade em estoque: "))

    # Gera um id para a carta
    card_id = len(cards) + 1

    card = Card(card_id, games[game], name, rarities[rarity], price, stock)

    cards.append(card)

    repository.save_cards(cards)


def list_cards():

    cards = repository.load_cards()

    print("\n" + "=" * 40)
    for card in cards:
        print(card)
    print("=" * 40 + "\n")


def list_cards_by_game():

    cards = repository.load_cards()

    display_games()
    game = int(input("Digite o jogo desejado: "))

    print("\n" + "=" * 40)
    for card in cards:
        if card.game.upper() == games[game].upper():
            print(card)
    print("=" * 40)


def list_cards_by_rarity():

    cards = repository.load_cards()

    display_rarities()
    rarity = int(input("Digite a raridade desejada: "))

    print("\n" + "=" * 40)
    for card in cards:
        if card.rarity.upper() == rarities[rarity].upper():
            print(card)
    print("=" * 40)


def find_card_by_id():

    cards = repository.load_cards()

    id = int(input("Digite o id da carta: "))
    for card in cards:
        if card.id == id:
            print("\n" + "=" * 40)
            print(card)
            print("=" * 40 + "\n")


def sell_card():

    cards = repository.load_cards()

    id = int(input("Digite o id da carta: "))
    quantity = int(input("Digite a quantidade a ser vendida: "))

    for card in cards:
        if card.id == id:
            if card.stock >= quantity:
                card.stock -= quantity
                card.sold += quantity
            else:
                print("\n[ERRO] - Estoque insuficiente")
                return

    repository.save_cards(cards)


def stock_replacement():

    cards = repository.load_cards()

    id = int(input("Digite o id da carta: "))
    quantity = int(input("Digite a quantidade a ser reposta: "))

    for card in cards:
        if card.id == id:
            card.stock += quantity

    repository.save_cards(cards)


def sales_report():

    cards = repository.load_cards()

    sold_cards = []

    for card in cards:
        if card.sold != 0:
            sold_cards.append(card)

    total_sales = 0  # Soma total das vendas
    total_revenue = 0  # Receita total

    print("\n" + "=" * 50)
    print("RELATÓRIO DE VENDAS".center(50))
    print("=" * 50)

    for card in sold_cards:

        card_sales = card.sold  # Quantidade de cartas vendidas
        card_revenue = card.sold * card.price  # Receita gerada pela venda

        total_sales += card_sales
        total_revenue += card_revenue

        print(f"\nCarta: {card.name}")
        print(f"Jogo: {card.game}")
        print(f"Raridade: {card.rarity}")
        print(f"Preço Unitário: R$ {card.price:.2f}")
        print(f"Unidades Vendidas: {card_sales}")
        print(f"Receita Gerada: R$ {card_revenue:.2f}")
        print("-" * 50)

    print("\n" + "=" * 50)
    print("RESUMO GERAL".center(50))
    print("=" * 50)
    print(f"\nTotal de Unidades Vendidas: {total_sales}")
    print(f"Receita Total: R$ {total_revenue:.2f}")
    print("=" * 50 + "\n")


def menu():

    while True:
        print("\n" + "=" * 40)
        print("MENU".center(40))
        print("=" * 40)
        print("1 - Cadastrar Carta")
        print("2 - Listar Cartas")
        print("3 - Listar Cartas por Jogo")
        print("4 - Listar Cartas por Raridade")
        print("5 - Buscar Carta por id")
        print("6 - Vender Carta")
        print("7 - Reposição de Estoque")
        print("8 - Relatório de Vendas")
        print("9 - Sair")
        print("=" * 40 + "\n")

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
            case 6:
                sell_card()
            case 7:
                stock_replacement()
            case 8:
                sales_report()
            case 9:
                print("\nSaindo...")
                break
            case _:
                print("\nOpção inválida")


if __name__ == "__main__":
    menu()
