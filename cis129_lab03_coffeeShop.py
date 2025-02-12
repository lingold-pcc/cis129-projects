# cis129_lab03_coffeeShop.py
"""printing a receipt including number of coffees and muffins bought, the price of those coffees and muffins, the tax, and the total price"""

# read ammount of coffees
coffees_ammount = int(input("How many coffees would you like? "))

# read ammount of muffins
muffins_ammount = int(input("How many muffins would you like? "))

# read ammount of croissants
croissants_ammount = int(input("How many croissants would you like? "))

# read ammount of bagels
bagels_ammount = int(input("How many bagels would you like? "))

# finding the price of the coffees
coffees_price = coffees_ammount * 5.00

# finding the price of the muffins
muffins_price = muffins_ammount * 4.00

# finding the price of the croissants
croissants_price = croissants_ammount * 3.00

# finding the price of the bagels
bagels_price = bagels_ammount * 3.50

# adding the price of the menu items purchased together
total_price_without_tax = coffees_price + muffins_price + croissants_price + bagels_price

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
Number of croissants bought?
""", croissants_ammount, """
Number of bagels bought?
""", bagels_ammount, """
***************************************
\n
***************************************
My Coffee and Muffin Shop Receipt
""", coffees_ammount, """ Coffee at $5 each: $  """, coffees_price, """
""", muffins_ammount, """ Muffins at $4 each: $ """, muffins_price, """
""", croissants_ammount, """ Croissants at $3 each: $ """, croissants_price, """
""", bagels_ammount, """ Bagels at $3.50 each: $ """, bagels_price, """
6% tax: $ """, tax_ammount, """
---------
Total: $ """, total_price_with_tax, """
Thank you for your pruchase! Have a nice day.
***************************************""")

