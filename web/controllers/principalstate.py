import reflex as rx


class PrincipalState(rx.State): # les variables son les visuals de la pagina
    count: int = 0
    color: str = "red"
    text: str ="Mati"
    #alumnes: list[str] = ["Dani", "Fallou", "Carlos", "Alba", "Mati", "Houssam", "Damià", "Guillem"]

    @rx.event
    def increment(self, value):
        self.count += value
        if self.count % 2 == 0:
            self.color = "green"
        else:
            self.color = "red"
    
    @rx.event
    def strat_increment(self):
        self.count = 0

    @rx.event
    def update_text(self, new_text: str):
        self.text = new_text

