# Problem 04
# Change in the Least Number of Notes & Coins

amount = 123.67
amount_cents = int(amount * 100)

# $100 $50 $20 $10 $5 $2 $1 50c 20c 10c 5c
hundreds = 0
if amount_cents > 10000:
    hundreds = amount_cents // 10000
    amount_cents = amount_cents % 10000

fifties = 0
if amount_cents > 5000:
    fifties = amount_cents // 5000
    amount_cents = amount_cents % 5000

twenties = 0
if amount_cents > 2000:
    twenties = amount_cents // 2000
    amount_cents = amount_cents % 2000

tens = 0
if amount_cents > 1000:
    tens = amount_cents // 1000
    amount_cents = amount_cents % 1000

fives = 0
if amount_cents > 500:
    fives = amount_cents // 500
    amount_cents = amount_cents % 500

twos = 0
if amount_cents > 200:
    twos = amount_cents // 200
    amount_cents = amount_cents % 200

ones = 0
if amount_cents > 100:
    ones = amount_cents // 100
    amount_cents = amount_cents % 100

# etc for the coins...

print(f"$100 x {hundreds}")
print(f"$50  x {fifties}")
print(f"$20  x {twenties}")
print(f"$10  x {tens}")
print(f"$5  x {fives}")
print(f"$2  x {twos}")
print(f"$1  x {ones}")
