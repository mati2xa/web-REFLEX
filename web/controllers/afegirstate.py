import  reflex as rx
from ..models import Product

class AfegirState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        with rx.session() as session:
            session.add(
                Product(
                    stock=form_data["stock_product"],
                    name=form_data["name_product"],
                    price=form_data["price_product"],
                    type=form_data["type_product"],
                )
            )
            session.commit()
        return rx.redirect("/llistat")
 
