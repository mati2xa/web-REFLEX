import reflex as rx
from ..models import Product

class ConsultarState(rx.State):
    form_data: dict = {}
    actual_product: Product = None

    @rx.var
    def get_codi(self) -> str:
        return self.router.page.params.get("codi")

    @rx.event
    def get_product(self):
        with rx.session() as session:
            self.actual_product = session.exec(
                Product.select().where(
                    Product.id == int(self.get_codi)
                )
            ).one_or_none()

    @rx.event
    def handle_submit_update(self):
        with rx.session() as session:
            product = session.exec(
                Product.select().where(
                    Product.id == int(self.get_codi)
                )
            ).one_or_none()
            product.stock = self.actual_product.stock
            product.name = self.actual_product.name
            product.price = self.actual_product.price
            product.type = self.actual_product.type
            session.add(product)
            session.commit()

        return rx.redirect("/llistat")
    
    @rx.event
    def handle_submit_delete(self):
        with rx.session() as session:
            product = session.exec(
                Product.select().where(
                    Product.id == int(self.get_codi)
                )
            ).first()
            session.delete(product)
            session.commit()

        return rx.redirect("/llistat")
    
    @rx.event
    def update_stock(self,value):
        self.actual_product.stock = int(value)

    @rx.event
    def update_name(self,value):
        self.actual_product.name = value

    @rx.event
    def update_price(self,value):
        self.actual_product.price = float(value)

    @rx.event
    def update_type(self,value):
        self.actual_product.type = value