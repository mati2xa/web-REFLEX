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
                    codi=form_data["codi_product"],
                    nom=form_data["nom_product"],
                    preu=form_data["preu_product"],
                )
            )
            session.commit()
        return rx.redirect("/llistat")
 
