# Problem 01
# Salary Calculator
#
# TODO: given a pay rate calculate the gross pay for
# an employee who works on a casual basis

# HINT: remove "magic numbers"
# HINT: Reusable - ask the user

pay_rate = None
hours_worked = None

while hours_worked is None:
    try:
        hours_worked = input("Enter hours worked:")
        hours_worked = float(hours_worked)
    except ValueError:
        print("ERROR: Please enter a number value")
        hours_worked = None

while pay_rate is None:
    try:
        pay_rate = float(input("Enter Pay Rate $"))
    except ValueError:
        print("ERROR: Please enter a number value")
        pay_rate = None


gross_pay = pay_rate * hours_worked
hours_worked_string = f"{hours_worked}hrs"

print("-"*40)
# print(hours_worked, "hrs at $", pay_rate, "Gross Pay is $", gross_pay)
print(f"{hours_worked_string} "
      f"at ${pay_rate:0.2f} "
      f"Gross Pay is ${gross_pay:0.2f}")

