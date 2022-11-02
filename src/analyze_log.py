import csv
from src.track_orders import TrackOrders


def analyze_log(file_path: str):
    if not file_path.endswith(".csv"):
        raise NotImplementedError(f"Extensão inválida:'{file_path}'")

    data = ({
        "cliente": [],
        "pedido": [],
        "dia": [],
    })

    try:
        analyze = TrackOrders()
        with open(file_path, encoding="utf-8") as file:
            file_reader = csv.reader(file)
            for c, p, d in file_reader:
                data["cliente"].append(c)
                data["pedido"].append(p)
                data["dia"].append(d)
                analyze.add_new_order(c, p, d)
        all_dishes = [dish for dish in data["pedido"] if dish not in all_dishes]
        
        # maria_pratos = [ordem["pedido"] for ordem in data if ordem["cliente"] == "maria" and ordem["pedido"] not in maria_pratos]
        maria_favorite_dish = analyze.get_most_ordered_dish_per_customer("maria")
        arnaldo_burger_eater = analyze.get_most_ordered_dish_per_customer("arnaldo")
        joao_dishes_unordered = analyze.get_never_ordered_per_customer("joao")
        joao_days_away = analyze.get_days_never_visited_per_customer("joao")

        with open("data/mkt_campaign.txt", "w") as file:
            file.write(
                f"{maria_favorite_dish}\n",
                f"{arnaldo_burger_eater}\n",
                f"{joao_dishes_unordered}\n",
                f"{joao_days_away}\n",
            )
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{file_path}'")

    
