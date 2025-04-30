import reflex as rx
from ..controllers.consultarstate import ConsultarState

def form_add_product():
    return rx.vstack(
            rx.form(
                rx.vstack(
                    rx.input(
                        value=ConsultarState.actual_product.codi,
                        on_change=ConsultarState.update_codi,
                        placeholder="Codi",
                        name="codi_product",
                    ),
                    rx.input(
                        value=ConsultarState.actual_product.nom,
                        placeholder="Nom",
                        name="nom_product",
                    ),
                    rx.input(
                        value=ConsultarState.actual_product.preu,
                        placeholder="Preu",
                        name="preu_product",
                    ),
                    rx.hstack(
                        rx.button("Modificar", type="button",on_click=ConsultarState.handle_submit_update),
                        rx.button("Eliminar", type="button",color_scheme="red",on_click=ConsultarState.handle_submit_delete),
                )    
                ),
                on_submit=ConsultarState.handle_submit,
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