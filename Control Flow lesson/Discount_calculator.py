purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount >= 1000;
    discount = 0.1                          # 10% of total purchase
elif purchase_amount >= 500:
    discount = 0.05                         # 5% of total purchase
else: 
    discount = 0.0                          # No discount   
    
final_price = purchase_amount * (1 - discount)

print(f"Final price after discount: ${final_price}")