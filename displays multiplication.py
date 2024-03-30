# This Python code displays multiplication tables from 2 to 20.

# Create a function to print the multiplication table of a number.
def print_table(number):
    # Iterate over the numbers from 1 to 12.
    for i in range(1, 13):
        # Print the product of the number and the current number.
        print(f"{number} x {i} = {number * i}")
# Iterate over the numbers from 2 to 20.
for i in range(2, 21):
    # Print the multiplication table of the current number.
    print(f"Multiplication table of {i}:")
    print_table(i)
    print()        