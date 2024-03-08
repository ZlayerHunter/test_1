from .coordinates import Coordinates
import uuid


class Order:
    def __init__(self, point_start, point_end, cost):
        self.p_start = Coordinates(*point_start)
        self.p_end = Coordinates(*point_end)
        self.cost = cost
        self.status = "queued"
        self.name = uuid.uuid4()
        self.courier = None

    def __str__(self):
        text = f"> Order cost: {self.cost}, Status: {self.status}\n"
        text += f"Start point: {self.p_start.__str__()}\n"
        text += f"End point: {self.p_end.__str__()} <"
        return text

    def __repr__(self):
        text = f"> Order Cost: {self.cost} "
        text += f"{self.p_start.__str__()} "
        text += f"{self.p_end.__str__()} <"
        return text

    def get_nearest_orders(self, orders):
        result = {}
        for order in orders:
            if order.status == "queued":
                result[self.p_end - order.p_start] = order
        return dict(sorted(result.items()))
    
    def get_nearest_order(self, orders):
        for order in self.get_nearest_orders(orders).values():
            return order

    def get_nearest_courier(self, couriers):
        result = {}
        for courier in couriers:
            if courier.status == "idle":
                result[self.p_start - courier.coordinates] = courier
        couriers = dict(sorted(result.items()))
        for courier in couriers.values():
            return courier
