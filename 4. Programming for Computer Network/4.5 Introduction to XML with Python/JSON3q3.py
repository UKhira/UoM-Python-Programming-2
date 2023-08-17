import requests
import json

# API details
base_url = "http://host1.open.uom.lk:8080"
update_product_url = f"{base_url}/api/products/3"  # Replace 'product_id' with the actual product ID

# Updated product data
updated_product_data = {
    "productName": "Araliya Basmathi Rice",
    "description": "White Basmathi Rice imported from Pakistan. High-quality rice with extra fragrance. Organically grown.",
    "category": "Rice",
    "brand": "Araliya",  # Updated brand
    "expiredDate": "2023.05.04",
    "manufacturedDate": "2022.02.20",
    "batchNumber": 324567,
    "unitPrice": 1020,
    "quantity": 200,
    "createdDate": "2022.02.24"
}

# Send PUT request to update the product
response = requests.put(update_product_url, json=updated_product_data)

# Print the JSON response
print("JSON Response:")
print(json.dumps(response.json(), indent=4))
