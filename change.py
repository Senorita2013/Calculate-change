def calculate_change(bill,paid):
    return paid - bill

bill_amount = 2.50
paid_amount = 4.00

change = calculate_change(bill_amount,paid_amount)
print("The shopkeeper should return:",change,"dollars")