import reflex as rx
from ..controllers.consultarstate import ConsultarState

def form_add_product():
    return rx.vstack(
            rx.form(
                rx.vstack(
                    rx.input(
                        value=ConsultarState.actual_product.stock,
                        on_change=ConsultarState.update_stock,
                        placeholder="Stock",
                        name="stock_product",
                    ),
                    rx.input(
                        value=ConsultarState.actual_product.name,
                        on_change=ConsultarState.update_name,
                        placeholder="Nom",
                        name="name_product",
                    ),
                    rx.input(
                        value=ConsultarState.actual_product.price,
                        on_change=ConsultarState.update_price,
                        placeholder="Preu",
                        name="price_product",
                    ),
                    rx.input(
                        value=ConsultarState.actual_product.type,
                        on_change=ConsultarState.update_type,
                        placeholder="Tipus",
                        name="type_product",
                    ),
                    rx.hstack(
                        rx.button("Modificar", type="button",on_click=[ConsultarState.handle_submit_update,rx.toast("Producto Modificado!")]),
                        rx.button("Eliminar", type="button",color_scheme="red",on_click=[ConsultarState.handle_submit_delete,rx.toast("Producto Eliminado!")]),
                )    
                ),
                reset_on_submit=True,
            ),
    )
def consultar_producte() -> rx.Component:
    return rx.container(
            rx.vstack(
                rx.heading("Modificar"),
                form_add_product(),
            )            
        ),