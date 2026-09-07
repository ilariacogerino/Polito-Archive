from dataclasses import dataclass
from datetime import datetime


@dataclass
class Sale:
    Retailer_code: int
    Product_number: int
    Product_brand: str
    Date: datetime
    Quantity: int
    Unit_sale_price: int
    Revenue: int

    def __str__(self):
        return f'Data: {self.Date}, Ricavo: {self.Revenue}, Retailer: {self.Retailer_code}, Product: {self.Product_number}'
