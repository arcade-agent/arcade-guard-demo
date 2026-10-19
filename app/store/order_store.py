from app.domain import Order


class OrderStore:
    def __init__(self):
        self._orders: dict[int, Order] = {}
        self._next_id = 1

    def save(self, order: Order) -> int:
        self._orders[order.id] = order
        return order.id

    def get(self, order_id: int) -> Order | None:
        return self._orders.get(order_id)

    def _generate_id(self) -> int:
        id_val = self._next_id
        self._next_id += 1
        return id_val

    def create(self, user_id: str, total: float) -> Order:
        order = Order(id=self._generate_id(), user_id=user_id, total=total)
        self.save(order)
        return order
