from product import product_details

def test_product_details():
    result = product_details("P101", "Wireless Mouse", 15, 1299.00)

    expected_output = (
        "Product ID: P101\n"
        "Product Name: Wireless Mouse\n"
        "Quantity: 15\n"
        "Price: 1299.0"
    )
    assert result == expected_output