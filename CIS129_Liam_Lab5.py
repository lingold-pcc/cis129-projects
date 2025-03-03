# Lab 5 The Bottle Return Program

# Step 1: Declare variables below 
totalBottles = 0 # total number of bottles
counter = 1 # number of days into the week
todayBottles = 0 # number of bottles returned on a day
totalPayout = 0 # total payout
keepGoing = 'y' # used to run the program again


    # Step 2: Loop to run program again
while keepGoing == 'y':
    # Step 3: Code to set value of variables
    totalBottles = 0
    todayBottles = 0
    counter = 1
    while counter < 8:
        todayBottles = int(input(f'Enter number of bottles returned for day #{counter}: '))
        counter += 1
    # code to set value of variable totalBottles
        totalBottles += todayBottles
    # code to set value of variable totalPayout
        totalPayout = totalBottles * .1
# code to print the number of total bottles and total payout
    print('Total number of bottles collected is', totalBottles)
    print(f'Total payout is ${totalPayout:.1f}')

    print('Do you want to enter another week’s worth of data?')
    keepGoing = input('(Enter y or n): ')
      		
