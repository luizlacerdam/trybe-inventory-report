from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json
import csv
class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path
    @abstractmethod
    def import_data(self) -> list[Product]:
        pass

class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path) as file:
            data = json.load(file)
            products = []
            for product in data:
                products.append(Product(**product))
            return products
    


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path) as file:
            data = csv.DictReader(file)
            products = []
            for product in data:
                products.append(Product(**product))
            return products


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}


