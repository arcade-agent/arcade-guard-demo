from app.store import OrderStore
from app.domain import Order


class OrderService:
    def __init__(self, store: OrderStore | None = None):
        self._store = store if store is not None else OrderStore()

    def place_order(self, user_id: str, total: float) -> int:
        order = self._store.create(user_id, total)
        return order.id

    def get_order(self, order_id: int) -> dict | None:
        order = self._store.get(order_id)
        if order is None:
            return None
        return {"id": order.id, "total": order.total}
