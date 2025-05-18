import reflex as rx

def conocenos() -> rx.Component:
    return rx.box(
        rx.color_mode.button(position="top-right"),
        rx.box(
            rx.image(
                src="/pccommm.png",
                width="100vw",
                height="100vh",
                object_fit="cover",
                border_radius="0",
            ),
            rx.link(
                rx.button("Principal", color_scheme="blue", border_radius="md"),
                href="/",
                style={
                    "position": "absolute",
                    "top": "50%",
                    "right": "5%",  # movido hacia la derecha con un margen desde el borde
                    "transform": "translateY(-50%)",  # solo centrar verticalmente
                    "z_index": "1"
                }
            ),
            position="relative",
            width="100vw",
            height="100vh",
            overflow="hidden",
        ),
        position="relative",
        width="100vw",
        height="100vh",
        margin="0",
        padding="0",
        style={"overflow": "hidden"},
    )

