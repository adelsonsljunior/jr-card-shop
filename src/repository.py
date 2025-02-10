import csv
from card import Card

filename = "data/cards.csv"


def load_cards():

    cards = []

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                card = Card(
                    id=int(row["id"]),
                    game=row["game"],
                    name=row["name"],
                    rarity=row["rarity"],
                    price=float(row["price"]),
                    stock=int(row["stock"]),
                    sold=int(row["sold"]),
                )
                cards.append(card)
        print("\n[INFO] - Cartas carregadas do arquivo CSV com sucesso!")
    except FileNotFoundError:
        print("\n[ERRO] - Arquivo CSV não encontrado. Iniciando com lista vazia.")

    return cards


def save_cards(cards):
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            # Define o cabeçalho do CSV
            fieldnames = ["id", "game", "name", "rarity", "price", "stock", "sold"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Escreve o cabeçalho
            writer.writeheader()

            # Escreve cada carta no arquivo CSV
            for card in cards:
                writer.writerow({
                    "id": card.id,
                    "game": card.game,
                    "name": card.name,
                    "rarity": card.rarity,
                    "price": card.price,
                    "stock": card.stock,
                    "sold": card.sold,
                })
        print("\n[INFO] - Cartas salvas no arquivo CSV com sucesso!")
    except Exception as e:
        print(f"\n[ERRO] - Ocorreu um erro ao salvar o arquivo CSV: {e}")
