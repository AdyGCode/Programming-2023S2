# Problem 04
# Change in the Least Number of Notes & Coins

amount = 399.99
amount_cents = int(amount * 100)

# $100 $50 $20 $10 $5 $2 $1 50c 20c 10c 5c
names = ["$100", "$50", "$20", "$10", "$5", "$2", "$1",
         "50c", "20c", "10c", "5c"]
denominations = [10000, 5000, 2000, 1000, 500, 200, 100,
                 50, 20, 10, 5]
quantities = [None] * len(denominations)

for count in range(0, len(denominations)):
    number_of_denomination = 0
    denomination_cents = denominations[count]
    if amount_cents > denomination_cents:
        number_of_denomination = amount_cents // denomination_cents
        amount_cents = amount_cents % denomination_cents
    quantities[count] = number_of_denomination

for count in range(0, len(denominations)):
    quantity = quantities[count]
    name = names[count]
    print(f"{name:8} x {quantity}")

print(f"we are unable to convert {amount_cents} cents")
