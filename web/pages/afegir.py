import reflex as rx
from ..controllers import principalstate
from ..controllers.afegirstate import AfegirState

def form_add_producte():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Codi del producte",
                    name="codi_product",
                ),
                rx.input(
                    placeholder="Nom del producte",
                    name="nom_product",
                ),
                rx.input(
                    placeholder="Preu del producte",
                    name="preu_product",
                ),
                rx.button("AFEGIR", type="submit"),
            ),
            on_submit=AfegirState.handle_submit,
            reset_on_submit=True,
        ),
    )

def afegir_producte() -> rx.Component:
    return rx.container(
        rx.text("Introdueix els valors"),
        form_add_producte()
    )