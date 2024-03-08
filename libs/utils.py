import copy
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed, wait as wait_future


def t2d(val):
    return val/60

def res_to_grad(res):
    grad = int(res.group(1))
    min = int(res.group(2))
    sec = float(res.group(3))
    return grad + t2d(min) + t2d(t2d(sec))

def var_1(couriers, orders):
    def get_idle_courier(couriers):
        for courier in couriers:
            if courier.status == "idle":
                return courier
    courier = get_idle_courier(couriers)
    courier.get_nearest_order(orders)
    courier.do_work
    return order

def var_1_task_manager(count_couriers, count_orders, couriers, orders):
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=count_couriers) as executor:
        tasks = [executor.submit(var_1, couriers, orders) for _ in range(count_orders)]
        results = as_completed(tasks)
    return time.time() - start_time

def create_map(orders):
    result = None
    true_result = {}
    for _ in range(3):
        if result is None:
            result = [orders.pop()]
        for i in range(len(orders)):
            order = result[i].get_nearest_order(orders)
            result.append(order)
            index = orders.index(order)
            del orders[index]
        temp_sum = sum(distance_beetwen(result))
        true_result[temp_sum] = copy.copy(result)
        orders = result
        result = [distance_beetwen(result, return_max_elem=True)]
    key = min([sum for sum in true_result.keys()])
    return true_result[key]

def distance_beetwen(orders, return_max_elem=False):
    result = []
    for i, order in enumerate(orders[:-1]):
        result.append(order.p_end - orders[i + 1].p_start)
    if return_max_elem:
        index = result.index(max(result))
        return orders.pop(index + 1)
    else:
        return result

def split_orders(count_couriers, count_orders, orders):
    if ostatok := count_orders % count_couriers:
        chunk = count_orders // count_couriers
        orders_split = []
        i = 0
        for _ in range(count_couriers):
            if ostatok != 0:
                orders_split.append(orders[i:i + chunk + 1])
                ostatok -= 1
                i += chunk + 1
            else:
                orders_split.append(orders[i:i + chunk])
                i += chunk
        orders_split = [orders for orders in orders_split if orders != []]
    else:
        chunk = count_orders // count_couriers
        orders_split = [orders[i * chunk:i * chunk + chunk] for i in range(count_couriers)]
    return orders_split

def var_2_task_manager(count_couriers, couriers, orders_split):
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        futures = []
        for orders in orders_split:
            future = executor.submit(
                    var_2, couriers, orders)
        results = as_completed(futures)
    return time.time() - start_time

def var_2(couriers, orders):
    courier = orders[0].get_nearest_courier(couriers)
    courier.orders = orders
    for order in orders:
        courier.get_order(order)
        courier.do_work
    return courier

def get_all_orders(couriers):
    for c in couriers:
        if c.orders:
            for order in c.orders:
                yield order

