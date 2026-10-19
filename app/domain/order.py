from dataclasses import dataclass


@dataclass
class Order:
    id: int
    user_id: str
    total: float
