import reflex as rx
from rxconfig import config
from web.components import sidebar_bottom_profile
from web.pages import center_container, afegir_producte, consultar_producte, llistat
from .controllers.llistastate import LlistaState
from .controllers.consultarstate import ConsultarState

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
        sidebar_bottom_profile(),
        center_container(),
    )
    

def prova() -> rx.Component:
    return rx.container(
        sidebar_bottom_profile(),
        center_container(),
        rx.link("pagina principal", href = "/"),
    ),

def afegir() -> rx.Component:
    return rx.hstack(
        sidebar_bottom_profile(),
        afegir_producte(),
    ),

def llista() -> rx.Component:
    return rx.hstack(
        sidebar_bottom_profile(),
        llistat(),
    ),

def consultar() -> rx.Component:
    return rx.hstack(
        sidebar_bottom_profile(),
        consultar_producte(),
    ),


app = rx.App()
app.add_page(index)
app.add_page(llista, route="llistat",on_load = LlistaState.get_products)
app.add_page(afegir, route="afegir")
app.add_page(consultar, route="consultar/[codi]", on_load = ConsultarState.get_product)

