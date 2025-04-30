import reflex as rx

class Product(rx.Model,table=True):
    codi : int
    nom : str
    preu : float
