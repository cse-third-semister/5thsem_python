"""
 19. The program that you create for this exercise will begin by reading the cost of a meal ordered at a
 restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local
 tax rate when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount
 (without the tax). The output from your program should include the tax amount, the tip amount, and
 the grand total for the meal including both the tax and the tip. Format the output so that all of the
 values are displayed using two decimal places.
"""

cost = float(input("Enter the cost of the meal: "))


tax_rate = cost * 0.05  
tip = cost * 0.18      

total = cost + tax_rate + tip


print(f"Tax amount: {tax_rate:.2f}")
print(f"Tip amount: {tip:.2f}")
print(f"Total amount: {total:.2f}")


# Tax amount 5.0
# Tip amount 18.0
# Total amount 123.0