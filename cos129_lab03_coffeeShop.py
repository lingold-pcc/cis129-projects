# cis129_lab03_coffeeShop.py
"""printing a receipt including number of coffees and muffins bought, the price of those coffees and muffins, the tax, and the total price"""

# read ammount of coffees
coffees_ammount = int(input("How many coffees would you like? "))

# read ammount of muffins
muffins_ammount = int(input("How many muffins would you like? "))

# multiply the ammount of coffees by the price of one coffee
coffees_price = coffees_ammount * 5.00

#mulitply the ammount of muffins by the price of one muffin
muffins_price = muffins_ammount * 4.00

# adding the price of the coffees and muffins together
total_price_without_tax = coffees_price + muffins_price

# finding the tax
tax_ammount = total_price_without_tax * 0.06

# finding the final price
total_price_with_tax = tax_ammount + total_price_without_tax

# printing the information as a receipt
print("""**************************************
My Coffee and Muffin Shop
Number of coffees bought?
""", coffees_ammount, """
Number of muffins bought?
""", muffins_ammount, """
***************************************
\n
***************************************
My Coffee and Muffin Shop Receipt
""", coffees_ammount, """ Coffee at $5 each: $  """, coffees_price, """
""", muffins_ammount, """ Muffins at $4 each: $ """, muffins_price, """
6% tax: $ """, tax_ammount, """
---------
Total: $ """, total_price_with_tax, """
***************************************""")

