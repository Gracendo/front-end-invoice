import json
import requests

from .constants import SERVER_URL

class Order:
    ENDPOINT = "/order/"

    def __init__(self, order_id=None,Date=None   **kwargs) -> None:
        self.order_id= order_id
        self.Date =Date
        
        self.files = []

    def save(self):
        url = f"{SERVER_URL}{self.ENDPOINT}"

        payload = {'Date': self.Date,
        }
        files=[
        ('files',('Nguh Prince ID recto.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID recto.jpg','rb'),'image/jpeg')),
        ('files',('Nguh Prince ID verso.jpg',open('/C:/Users/Jamie/Downloads/Nguh Prince ID verso.jpg','rb'),'image/jpeg'))
        ]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        data = json.loads(response.text)
        self.order_id= data['order_id']

    def read(order_id=None):
        url = f"{SERVER_URL}{__class__.ENDPOINT}"
        url += order_id if order_id else ''

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)

        if order_id:
            order = __class__(**response)
            return order
        else:
           orders = []

            for result in response:
               order = __class__(**result)
               orders.append(order)
            
            return orders

    def delete(self):
        url = f"{SERVER_URL}{self.ENDPOINT}{self.order_id}"

        payload, headers = {}, {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        try:
            response.raise_for_status()

            self.order_id = None
        except Exception:
            raise exception