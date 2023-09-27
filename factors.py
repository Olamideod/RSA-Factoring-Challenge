#!/usr/bin/python3
import sys

# Function to factorize a number into two smaller numbers
def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

input_file = sys.argv[1]

try:
    with open(input_file, 'r') as file:
        for line in file:
            n = int(line.strip())  # Convert the line to an integer
            p, q = factorize(n)
            print(f"{n}={p}*{q}")

except FileNotFoundError:
    print(f"File '{input_file}' not found.")
    sys.exit(1)
except ValueError:
    print("Invalid input. Please provide a file containing natural numbers greater than 1.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)

