# -------------------------------------------
# Exercise 4: Decision-Making Program
# -------------------------------------------
# In this exercise, you will write a program that makes decisions based on user input.
# You will practice combining Boolean logic with conditional statements.
#
# Goals:
# - Ask the user for input
# - Use conditions to decide what to do
# - Print messages based on the conditions
# - Test your program with different inputs
#
# -------------------------------------------

# Step 1: Simple decision
# -----------------------
# Ask the user to enter a number.
# Decide something about the number using an if statement.

# Example of syntax (no answer given):
# if some_condition:
#     print("Message for True condition")

# TODO:
# 1. Ask the user to type a number and store it in a variable.
# 2. Use an if statement to check something about the number.
# 3. Print a message if the condition is True.

# Write your code below:


num1 = int(input("Step 1: Type in a number: "))
if num1 > 0:
    print("Your number is greater than 0")


# Step 2: Add else
# ----------------
# Sometimes we need to print a different message if the condition is False.

# Example of syntax (no answer given):
# if some_condition:
#     print("Message if True")
# else:
#     print("Message if False")

# TODO:
# 1. Add an else statement to your code from Step 1.
# 2. Print a different message if the number does not meet your condition.

# Write your code below:


num2 = int(input("Step 2: Input another number: "))
if num2 > 0: 
    print("Your number is greater than zero")
else:
    if num2 < 0: 
        print("Your number is less than 0")   


# Step 3: Multiple conditions
# ---------------------------
# You can check more than one condition using elif or Boolean operators.

# Example of syntax (no answer given):
# if condition1:
#     print("Message 1")
# elif condition2:
#     print("Message 2")
# else:
#     print("Message 3")

# TODO:
# 1. Extend your program to check multiple conditions.
# 2. Print different messages for each case.
# 3. Test your program with different inputs to see all possible messages.

# Write your code below:


num3 = int(input("Step 3: Please enter another number: "))
if num3 > 0: 
    print("Your number is greater than 0")
elif num3 == 0:
    print ("Your number is equal to 0")
else: 
    print("Your number is less than 0")



# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# When you have finished this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run the following commands:
#    git add Ex4_decisions.py
#    git commit -m "Completed decision-making program exercise"
#    git push origin main
# Check GitHub to see your changes.
# -------------------------------------------

# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1:
# Ask the user for a number and a word.
# Use conditions to print a message only if the number is greater than a value
# AND the word matches a stored word.

# Extension 2:
# Ask the user for a number.
# Print different messages depending on:
# - number is positive
# - number is zero
# - number is negative

# Extension 3 (more challenging):
# Create a small quiz:
# - Ask the user a multiple-choice question.
# - Check their answer and print "Correct!" or "Try again!".
# - Add another condition to give a special message if the answer is partially correct.

# Write your extension code below:

#Ext1


num4 = int(input("Ext 1: Please enter a number: "))
word1 = input("Now please enter a word: ")
if num4 > 4 and word1 == "pizza":
    print(f"Mmmmmmm. I would like {num4} pizzas too.")


#Ext2

num5 = int(input("Ext 2: Please enter a number: "))
if num5 > 0:
    print("Your number is positive!")
elif num5 == 0:
    print("Your number is 0, does that mean it's neither positive or negative?")
else:
    print("Your number is negative, but you don't have to be!")


#Ext3



# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# When you have finished this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run the following commands:
#    git add Ex4_decisions.py
#    git commit -m "Completed extension activities"
#    git push origin main
# Check GitHub to see your changes.
# -------------------------------------------
