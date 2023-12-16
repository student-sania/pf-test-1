# program no:1
# takes to integers as input
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
if num1%2==1 and num2%2==1:
    sum_of_square=(num1*num1)+(num2*num2)
    print(sum_of_square)
else:
    print("Calculation is not performed") 

# program no:2
# Get user-input for number 
number=int(input("Enter a number:")) 
factorial=1
current_number=1
# calculate the factorial using while loop
while current_number <= number:
    factorial*=current_number
    current_number+=1
    print(f"the factorial of {number} is: {factorial}") 

# program no: 3
import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Number of attempts allowed
    max_attempts = 5
    print("Welcome to the Guess the Number game!")
    print("Try to guess the number between 1 and 100.")

    for attempt in range(1, max_attempts + 1):
        # Get user input
        user_guess = int(input("Attempt {}: Enter your guess: ".format(attempt)))

        # Check if the guess is correct
        if user_guess == secret_number:
            print("Congratulations! You guessed the number.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    else:
        # This block executes if the loop completes without a 'break'
        print("Game over! You ran out of guesses. The correct number was {}.".format(secret_number))

# Run the game
guess_the_number()

# proram no:4
def calculate_restaurant_bill():
    # Get user input
    num_people = int(input("Enter the number of people: "))
    cost_per_meal = float(input("Enter the cost of each meal: $"))
    sales_tax_percentage = float(input("Enter the sales tax percentage: "))
    tip_percentage = float(input("Enter the tip percentage: "))

    # Calculate total cost of food
    total_food_cost = num_people * cost_per_meal

    # Calculate sales tax
    sales_tax = (sales_tax_percentage / 100) * total_food_cost

    # Calculate tip amount
    tip_amount = (tip_percentage / 100) * total_food_cost

    # Calculate total bill amount
    total_bill_amount = total_food_cost + sales_tax + tip_amount

    # Calculate total bill amount per person
    bill_amount_per_person = total_bill_amount / num_people

    # Print the results
    print("\nSummary:")
    print("Number of People: {}".format(num_people))
    print("Cost per Meal: ${}".format(cost_per_meal))
    print("Total Cost of Food: ${:.2f}".format(total_food_cost))
    print("Sales Tax Percentage: {}%".format(sales_tax_percentage))
    print("Total Sales Tax: ${:.2f}".format(sales_tax))
    print("Tip Percentage: {}%".format(tip_percentage))
    print("Total Tip Amount: ${:.2f}".format(tip_amount))
    print("Total Bill Amount: ${:.2f}".format(total_bill_amount))
    print("Bill Amount per Person: ${:.2f}".format(bill_amount_per_person))

# Run the program
calculate_restaurant_bill()

