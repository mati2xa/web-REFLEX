import reflex as rx
from ..controllers import principalstate
from ..controllers.afegirstate import AfegirState

def form_add_producte():
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Stock del producte",
                    name="stock_product",
                ),
                rx.input(
                    placeholder="Nom del producte",
                    name="name_product",
                ),
                rx.input(
                    placeholder="Preu del producte",
                    name="price_product",
                ),
                rx.input(
                    placeholder="Tipus de producte",
                    name="type_product",
                ),
                rx.button("AFEGIR", type="submit", on_click=rx.toast("Producto Añadido!")),
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