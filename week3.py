def calculate_discount():
    original_price= float(input("Please enter the original price of your item: "))
    discount_percent= float(input("Please enter your discount price: "))

    if discount_percent>=20:
        final_price= original_price-(original_price*discount_percent/100)
        print("Your final price is:", final_price)
    else:
        print("Your item is not eligible for discount. The price of your item is: ", original_price)

calculate_discount()

