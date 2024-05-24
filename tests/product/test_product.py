import pytest
from inventory_report.product import Product

mark = pytest.mark.dependency


@pytest.mark.dependency
def test_create_product() -> None:
    produto = Product(
        "1",
        "product name",
        "company name",
        "2021-09-06",
        "2024-09-17",
        "serial number",
        "storage instructions",
    )
    assert produto is not None
    assert produto.id == "1"
    assert produto.product_name == "product name"
    assert produto.company_name == "company name"
    assert produto.manufacturing_date == "2021-09-06"
    assert produto.expiration_date == "2024-09-17"
    assert produto.serial_number == "serial number"
    assert produto.storage_instructions == "storage instructions"
