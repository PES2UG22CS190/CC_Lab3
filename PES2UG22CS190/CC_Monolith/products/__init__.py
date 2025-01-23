from products import dao


class Product:
    __slots__ = ('id', 'name', 'description', 'cost', 'qty')

    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    products = dao.list_products()
    return [Product.from_dict(product) for product in products]


def get_product(product_id: int) -> Product:
    return Product.from_dict(dao.get_product(product_id))


def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
