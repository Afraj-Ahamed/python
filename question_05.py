def calculate_total(price, tax_rate=0.05, discount=0):
    discounted_price = price - discount
    tax_with_price = discounted_price * (1 + tax_rate)
    return round(tax_with_price,2)

total = calculate_total(price=100 , discount=10)
print(total)