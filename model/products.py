import json
import requests

from .constants import SERVER_URL

class Products:
    ENDPOINT = "/products/"

    def __init__(self, product_id=None,product_name=None,quantity=None,Date_stock=None, Unitprice=None,   **kwargs) -> None:
        self.product_id = product_id
        self.product_name =product_name
        self.quantity = quantity 
        self.Date_stock = Date_stock
        self.Unitprice = Unitprice
        self.files = []

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {'product_name': self.product_name,
        'quantity': self.quantity,
        'Date_stock': self.Date_stock,
        'Unitprice': self.Unitprice}
        files=[
        ('files',('Nguh Prince ID recto.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID recto.jpg','rb'),'image/jpeg')),
        ('files',('Nguh Prince ID verso.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID verso.jpg','rb'),'image/jpeg'))
        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        data = json.loads(response.text)
        self.product_id= data['product_id']

    def read(product_id=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += product_id if product_id else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)

        if product_id:
            Product = __class__(**response)
            return Product 
        else:
            Products = []

            for result in response:
                Product  = __class__(**result)
               Products.append(Product)
            
            return Products

g    def delete(self):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.product_id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.product_id = None
        except Exception:
            raise exception