import reflex as rx
from ..controllers import LlistaState
from ..models import Product

def show_product(product: Product):
    """Show a person in a table row."""
    return rx.table.row(
        rx.table.cell(rx.link(product.id, href=f"consultar/{product.id}")),
        rx.table.cell(product.stock),
        rx.table.cell(product.name),
        rx.table.cell(product.price),
        rx.table.cell(product.type),
    )

def foreach_table_example():
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Id inter"),
                rx.table.column_header_cell("Stock"),
                rx.table.column_header_cell("Nom"),
                rx.table.column_header_cell("Preu"),
                rx.table.column_header_cell("Tipus"),
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