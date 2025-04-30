import reflex as rx
from ..models import Product

class LlistaState(rx.State):
    products: list[Product]

    @rx.event
    def get_products(self):
        with rx.session() as session:
            self.products = session.exec(
                Product.select()
            ).all()