from inventory_report.product import Product

def test_product_report() -> None:
    id = "1"
    product_name = "product name"
    company_name = "company name"
    manufacturing_date = "2021-09-06"
    expiration_date = "2024-09-17"
    serial_number = "serial number"
    storage_instructions = "storage instructions"

    product = Product(
        id,
        product_name,
        company_name,
        manufacturing_date,
        expiration_date,
        serial_number,
        storage_instructions,
    )
    assert str(product) == (
        f"The product {id} - {product_name} "
        f"with serial number {serial_number} "
        f"manufactured on {manufacturing_date} "
        f"by the company {company_name} "
        f"valid until {expiration_date} "
        "must be stored according to the following instructions: "
        f"{storage_instructions}."
    )
