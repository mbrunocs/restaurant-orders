def extract_customer(customer: str, data):
    customer_data = dict({
        "name": customer.lower(),
        "visitas": [],
        "pedidos": [],
    })
    for order in data:
        if order[0] == customer.lower():
            customer_data["visitas"].append(order[2])
            customer_data["pedidos"].append(order[1])
    return customer_data


class TrackOrders:
    def __init__(self):
        self.orders = list()
    
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        customer_data = extract_customer(customer, self.orders)
        count = dict()
        for dish in customer_data["pedidos"]:
            if dish not in count:
                count[dish] = 1
            else:
                count[dish] += 1
        return max(count, key=count.get)

    def get_never_ordered_per_customer(self, customer):
        customer_data = extract_customer(customer, self.orders)
        count = dict()
        for dish in customer_data["pedidos"]:
            if dish not in count:
                count[dish] = 1
            else:
                count[dish] += 1
        return min(count, key=count.get)

    def get_days_never_visited_per_customer(self, customer):
        customer_data = extract_customer(customer, self.orders)
        days_opened = set(order[2] for order in self.orders)
        return days_opened.difference(customer_data["visitas"])

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

    def get_dish_orders_per_customer(self, customer, dish):
        pass
