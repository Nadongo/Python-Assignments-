def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent/100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
price = float(input("Enter the original price of the Item: "))
discount_percent =  float(input("Enter the percentage discount of the item: "))

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"The final price after a {discount_percent}% discount is: ${final_price:.2f}")
else:
    print(f"No discount applied the Original Price is: ${price:.2f}")