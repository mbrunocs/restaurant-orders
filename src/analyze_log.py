import csv
from src.track_orders import TrackOrders


def extract_customer(customer: str, data):
    customer_data = dict({
        "name": customer,
        "visitas": [],
        "pedidos": [],
    })
    for i, cliente in enumerate(data["cliente"]):
        if cliente == customer:
            customer_data["visitas"].append(data["dia"][i])
            customer_data["pedidos"].append(data["pedido"][i])
    return customer_data


def analyze_log(file_path: str):
    if not file_path.endswith(".csv"):
        raise NotImplementedError(f"Extensão inválida:'{file_path}'")

    data = ({
        "cliente": [],
        "pedido": [],
        "dia": [],
    })

    try:
        with open(file_path, encoding="utf-8") as file:
            file_reader = csv.reader(file)
            for c, p, d in file_reader:
                data["cliente"].append(c)
                data["pedido"].append(p)
                data["dia"].append(d)
        analyze = TrackOrders()
        all_dishes = [dish for dish in data["pedido"] if dish not in all_dishes]
        maria = extract_customer("maria", data)
        maria_pratos = [ordem["pedido"] for ordem in data if ordem["cliente"] == "maria" and ordem["pedido"] not in maria_pratos]

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{file_path}'")

    
