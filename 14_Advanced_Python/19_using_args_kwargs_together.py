def process_order(order_id, *items, **customer_details):
    print(f"Processing Order ID: {order_id}")
    
    print("\nItems in order:")
    for item in items:
        print(f"- {item}")
        
    print("\nCustomer Details:")
    for key, value in customer_details.items():
        print(f"- {key}: {value}")

process_order(101, "Laptop", "Mouse", "Keyboard", 
              name="Bhavesh", delivery_address="123 Python Lane, Mumbai")