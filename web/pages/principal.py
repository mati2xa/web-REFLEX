import reflex as rx
from ..controllers.principalstate import PrincipalState

#def center_container()-> rx.Component:
    #return rx.container(
        #rx.color_mode.button(position="top-right"),
        #rx.vstack(
            #rx.heading("Bienvenido " + PrincipalState.text, size="9"),
            #rx.input(
            #    default_value=PrincipalState.text,
             #   on_change=PrincipalState.update_text, # se actualiza al instante
            #),
            # rx.input(
            #     default_value=MyState.text,
            #     on_blur=MyState.update_text,  #s'actualitza quan surts de l'init
            # ),  
            #rx.hstack(
            #    rx.button("click me + 1",size="4", border_radius = "50px", on_click=lambda :PrincipalState.increment(1)),
            #    rx.button("click me + 5",size="4", border_radius = "50px", on_click=lambda :PrincipalState.increment(5)),
            #    rx.text(PrincipalState.count, color=PrincipalState.color, font_size = "40px"),
            #    rx.button("restart",size="4", color_scheme="red", border_radius = "50px", on_click=PrincipalState.strat_increment),
            #    align = "center"
            #),
            #rx.hstack(
                #rx.cond(
                #    PrincipalState.color == "red",
                #    rx.text("color vermell", color = "red"),
                #    rx.text("color verd", color = "green"),
                #),
                #align = "center"
            #),
            # rx.box(
            #     rx.foreach(MyState.alumnes, _render_alume) #llista d'alumnes
            # ),
            #spacing="4",
            #justify="center",
            #align = "center",   
            #min_height="85vh",
        #),
        #rx.logo(),
    #)



def center_container() -> rx.Component:
    return rx.box(
        rx.color_mode.button(position="top-right"),
        rx.box(
            rx.image(src="/pccomm.png", width="100%", max_width="1300px", border_radius="lg"),
            rx.link(
                rx.button("Conócenos", color_scheme="blue", border_radius="md"),
                href="/conocenos",
                style={
                    "position": "absolute",
                    "top": "50%",
                    "left": "50%",
                    "transform": "translate(-50%, -50%)",
                    "z_index": "1"
                }
            ),
            position="relative",
            width="1300px", # ocupa todo el espacio de su contenedor, no de la pantalla completa
            height="auto",
            margin_left="17em",
        ),
        align_items="center",
        justify_content="center",
        min_height="100vh",
        width="100%",  # NO uses 100vw porque eso ignora el sidebar
        style={
            "overflow": "hidden"
        }
    )

