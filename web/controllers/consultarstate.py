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
    def handle_submit(self):
        with rx.session() as session:
            product = session.exec(
                Product.select().where(
                    product.id == int(self.get_codi)
                )
            ).one_or_none()
            product.codi = self.actual_product.codi
            product.nom = self.actual_product.nom
            product.preu = self.actual_product.preu
            session.add(product)
            session.commit()

        return rx.redirect("/llistat")
    
    @rx.event
    def update_codi(self,value):
        self.actual_product.codi = int(value)