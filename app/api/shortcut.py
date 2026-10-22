from app.store.order_store import OrderStore


def count():
    return len(OrderStore()._orders)
