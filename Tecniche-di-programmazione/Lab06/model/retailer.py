from dataclasses import dataclass


@dataclass
class Retailer():
    Retailer_code: int
    Retailer_name: str
    Type: str
    Country: str

    def __str__(self):
        return self.Retailer_name