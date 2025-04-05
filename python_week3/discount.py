def main():
    # Get user input
    price = float(input("Enter the price: "))
    discount_percent = float(input("Enter the discount percentage in decimal: "))

    # Calculate discount
    discounted_price = calculate_discount(price, discount_percent)

    # Print result
    print(f"You are to pay: {discounted_price}")

def calculate_discount(price, discount_percent):
    if discount_percent > 20/100:
        discount = price - (price * discount_percent)
        return discount
    else:
        return price
    
if __name__ == "__main__":
    main()