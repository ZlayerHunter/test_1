from libs.generators import (
        generate_order,
        generate_courier,
        )
from libs.utils import (
        create_map,
        distance_beetwen,
        split_orders,
        var_1_task_manager,
        var_2_task_manager,
        )
import copy


def main():
    # Задаем количество заказок и курьеров
    count_orders = 20
    count_couriers = 3

    # Генерируем заказы и курьеров
    orders = [generate_order() for _ in range(count_orders)]
    couriers = [generate_courier() for _ in range(count_couriers)]

    # Копируем для второго теста
    # Сортируем список
    orders_2 = copy.deepcopy(orders)
    couriers_2 = copy.deepcopy(couriers)
    # Колдунство для второго алгоритма
    orders_2 = create_map(orders_2)
    orders_split = split_orders(
            count_couriers, count_orders, orders_2)

    # Запускаем курьеров по первому алгоритму
    # Каждый курьер берет ближайщий от себя заказ
    var_1 = var_1_task_manager(
            count_couriers, count_orders, couriers, orders)
    for _ in orders:
        print(_)

    # Запускаем курьеров по второму алгоритму
    # Каждый курьер берет ближайщий от себя заказ
    var_2 = var_2_task_manager(
            count_couriers, couriers_2, orders_split)
    for _ in orders_2:
        print(_)

    print("less is better")
    print("variant_1", var_1)
    print("variant_2", var_2)

if __name__ == "__main__":
    main()
