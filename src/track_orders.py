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


class TrackOrders:
    def __init__(self):
        self.orders = list()
    
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

    def get_dish_orders_per_customer(self, customer, dish):
        pass
