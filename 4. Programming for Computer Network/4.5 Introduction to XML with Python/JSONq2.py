import requests

# API details
base_url = "http://host1.open.uom.lk:8080"
get_products_url = f"{base_url}/api/products"  # Replace with the actual endpoint for retrieving products

# Send GET request to retrieve all products
response = requests.get(get_products_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    products_data = response.json().get("data", [])
    
    # Print the total number of products
    total_products = len(products_data)
    print("Total Number of Products:", total_products)
    
    # You can also print each product's details if needed
    for product in products_data:
        print("\nProduct ID:", product["id"])
        print("Product Name:", product["productName"])
        # Print other product details as needed
else:
    print("Failed to retrieve products. Status Code:", response.status_code)
