import reflex as rx

class Product(rx.Model,table=True):
    stock : int
    name : str
    price : float
    type : str
