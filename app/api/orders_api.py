from app.service import OrderService


class OrdersApi:
    def __init__(self):
        self._service = OrderService()

    def place_order(self, user_id: str, total: float) -> int:
        return self._service.place_order(user_id, total)

    def get_order(self, order_id: int) -> dict | None:
        return self._service.get_order(order_id)
