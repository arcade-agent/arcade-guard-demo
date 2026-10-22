from app.service import OrderService
from app.domain import Order


class OrdersApi:
    def __init__(self):
        self._service = OrderService()

    def place_order(self, user_id: str, total: float) -> int:
        return self._service.place_order(user_id, total)

    def get_order(self, order_id: int) -> dict | None:
        return self._service.get_order(order_id)

    def order_summary(self, order_id: int) -> str | None:
        data = self._service.get_order(order_id)
        if data is None:
            return None
        order = Order(id=data["id"], user_id="", total=data["total"])
        return f"order {order.id}: {order.total:.2f}"
