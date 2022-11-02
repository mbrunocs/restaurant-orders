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


def count_dishes(list_dishes, more_dishes=list()):
    if len(more_dishes) > 0:
        count = {x: 0 for x in count_dishes(more_dishes)}
    else:
        count = dict()
    for dish in list_dishes:
        if dish not in count:
            count[dish] = 1
        else:
            count[dish] += 1
    return count


class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        customer_data = extract_customer(customer, self.orders)
        dishes_order = count_dishes(customer_data["pedidos"])
        return max(dishes_order, key=dishes_order.get)

    def get_never_ordered_per_customer(self, customer):
        customer_data = extract_customer(customer, self.orders)
        all_dishes = set(order[1] for order in self.orders)
        return all_dishes.difference(set(customer_data["pedidos"]))

    def get_days_never_visited_per_customer(self, customer):
        customer_data = extract_customer(customer, self.orders)
        days_opened = set(order[2] for order in self.orders)
        return days_opened.difference(customer_data["visitas"])

    def get_busiest_day(self):
        days_orders = dict()
        for _, _, day in self.orders:
            if day not in days_orders:
                days_orders[day] = 1
            else:
                days_orders[day] += 1
        return max(days_orders, key=days_orders.get)

    def get_least_busy_day(self):
        days_orders = dict()
        for _, _, day in self.orders:
            if day not in days_orders:
                days_orders[day] = 1
            else:
                days_orders[day] += 1
        return min(days_orders, key=days_orders.get)

    def get_number_dish_ordered_per_customer(self, customer: str, dish: str):
        customer_data = extract_customer(customer, self.orders)
        dishes_order = count_dishes(customer_data["pedidos"])
        return dishes_order[dish]
