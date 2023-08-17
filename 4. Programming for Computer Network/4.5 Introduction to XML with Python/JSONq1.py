import requests
import json

# API details
base_url = "http://host1.open.uom.lk:8080"
create_product_url = f"{base_url}/api/products"  # Assuming /products is the endpoint for creating products

# Product data in JSON format
product_data = {
    "productName": "Araliya Basmathi Rice",
    "description": "White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
    "category": "Rice",
    "brand": "CIC",
    "expiredDate": "2023.05.04",
    "manufacturedDate": "2022.02.20",
    "batchNumber": 324567,
    "unitPrice": 1020,
    "quantity": 200,
    "createdDate": "2022.02.24"
}

# Send POST request to create a new product
response = requests.post(create_product_url, json=product_data)

# Print the response code
print(response.status_code)
