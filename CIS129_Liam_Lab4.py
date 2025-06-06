# Name: Liam Ingold
# Date: 2/21/2025
"""This script asks for the monthly sales and percent of sales increase to determine the various bonuses"""

# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase


# This code gets the monthly sales
monthlySales = float(input('Enter the monthly sales: '))

# This code gets the percent of increase in sales
salesIncrease = float(input('Enter percent of sales increase: '))
salesIncrease = salesIncrease / 100
                      
# This code determines the storeAmount bonus
if monthlySales >= 110000:
                     storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# This code determines the empAmount bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= 0.04:
    empAmount = 50
elif salesIncrease >= 0.03:
    empAmount = 40
else:
    empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible!')

