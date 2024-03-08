from .coordinates import Coordinates
import asyncio
import time
import uuid


class Courier:
    def __init__(self, point):
        self.coordinates = Coordinates(*point)
        koef = 1000/3600
        self.speed = koef * 6000 # km/h
        self.status = "idle"
        self.cur_order = None
        self.compl_orders = []
        self.name = uuid.uuid4()
        self.orders = None

    def __str__(self):
        text = f"> Courier Point: "
        text += f"{self.coordinates.__str__()}"
        text += f" Complete order: {len(self.compl_orders)} <"
        return text
    
    def get_nearest_orders(self, orders):
        result = {}
        for order in orders:
            if order.status == "queued":
                result[self.coordinates - order.p_start] = order
        return dict(sorted(result.items()))
    
    def get_nearest_order(self, orders):
        for order in self.get_nearest_orders(orders).values():
            print(f'{self.name} get order')
            order.status = "process"
            order.courier = self
            self.cur_order = order
            self.status = "work"
            return

    def get_order(self, order):
        print(f'{self.name} get order')
        if order.status =="queued":
            order.status = "process"
            order.courier = self
            self.cur_order = order
            self.status = "work"
            return

    @property 
    def do_work(self):
        if self.status == "work":
            get_time = (self.coordinates\
                    - self.cur_order.p_start) / self.speed
            print(f"{self.name} edu do order, primerno {int(get_time)} sec")
            time.sleep(get_time)
            print(f"{self.name} get order")
            self.status = "work"
            self.coordinates = self.cur_order.p_start
            work_time = (self.coordinates\
                    - self.cur_order.p_end)/ self.speed
            print(f"{self.name} going to end_point, primerno {int(work_time)}")
            time.sleep(work_time)
            print(f"{self.name} complete order")
            self.status = "idle"
            self.cur_order.status = "completed"
            self.coordinates = self.cur_order.p_end
            self.compl_orders.append(self.cur_order)
            self.cur_order = None
