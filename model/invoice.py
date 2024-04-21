import json
import requests

from .constants import SERVER_URL

class Invoices:
    ENDPOINT = "/products/"

    def __init__(self, invoice_id=None,invoice_name=None,quantity=None,Date_stock=None, Unitprice=None,   **kwargs) -> None:
        self.invoice_id = invoice_id
        self.invoice_name =invoice_name
        self.quantity = quantity 
        self.Date_stock = Date_stock
        self.Unitprice = Unitprice
        self.files = []

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {'invoice_name': self.invoice_name,
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
        self.invoice_id= data['invoice_id']

    def read(invoice_id=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += invoice_id if invoice_id else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)

        if invoice_id:
            Invoice = __class__(**response)
            return Invoice
        else:
            Invoices = []

            for result in response:
                Invoice  = __class__(**result)
               Invoice.append(Invoice)
            
            return Invoices

g    def delete(self):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.invoice_id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.invoice_id = None
        except Exception:
            raise exception