import csv
from src.track_orders import TrackOrders


def analyze_log(file_path: str):
    if not file_path.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida:'{file_path}'")

    analyze = TrackOrders()
    try:
        with open(file_path, encoding="utf-8") as file:
            file_reader = csv.reader(file)
            for c, p, d in file_reader:
                analyze.add_new_order(c, p, d)

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{file_path}'")
    except (KeyError, TypeError):
        raise KeyError()

    maria_favorite_dish = analyze.get_most_ordered_dish_per_customer("maria")
    arnaldo_burger_eater = analyze.get_number_dish_ordered_per_customer(
        "arnaldo", "hamburguer")
    joao_dishes_unordered = analyze.get_never_ordered_per_customer("joao")
    joao_days_away = analyze.get_days_never_visited_per_customer("joao")

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
f"""{maria_favorite_dish}
{arnaldo_burger_eater}
{joao_dishes_unordered}
{joao_days_away}""",
    )
