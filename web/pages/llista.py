import reflex as rx
from ..controllers import LlistaState
from ..models import Product

def show_product(product: Product):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(rx.link(product.codi, href=f"consultar/{product.id}")),
        rx.table.cell(product.nom),
        rx.table.cell(product.preu),
    )

def foreach_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Codi"),
                rx.table.column_header_cell("Nom"),
                rx.table.column_header_cell("Preu"),
            ),
        ),
        rx.table.body(
            rx.foreach(LlistaState.products, show_product)
        ),
        width="100%",
    )

def llistat() -> rx.Component:
    return rx.container(
            foreach_table_example()
        ),