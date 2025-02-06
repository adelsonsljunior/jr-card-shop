import csv
from card import Card

filename = "csvs/cards.csv"

cards = []

def get_cards():

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


def create_card(card):

    print("Marceline")