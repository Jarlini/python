def is_even_or_odd():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
is_even_or_odd()
# 2

def check_age_category():
    age = int(input("Enter your age: "))
    if age < 18:
        print("Minor")
    elif age <= 64:
        print("Adult")
    else:
        print("Senior")
check_age_category()
# 3. Temperature Advice: temperature_advice

def temperature_advice():
    temp = float(input("Enter the temperature in Celsius: "))
    if temp > 30:
        print("Hot")
    elif 15 <= temp <= 30:
        print("Warm")
    else:
        print("Cold")

# # Example usage
temperature_advice()
# 4. Grade Evaluation: evaluate_grade

def evaluate_grade():
    score = float(input("Enter the grade score: "))
    if 90 <= score <= 100:
        print("A")
    elif 80 <= score < 90:
        print("B")
    elif 70 <= score < 80:
        print("C")
    elif 60 <= score < 70:
        print("D")
    else:
        print("F")

# # Example usage
evaluate_grade()
# 5. Sum of List: sum_list

def sum_list():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    print("Sum of the numbers:", sum(numbers))
sum_list()

# Example usag
# 6. Print Multiples: print_multiples

def print_multiples():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# Example usage

# 7. Reverse String: reverse_string

def reverse_string():
    text = input("Enter a string: ")
    print("Reversed string:", text[::-1])
reverse_string()
# Example usage
# 8. Count Vowels: count_vowels

def count_vowels():
    text = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    print("Number of vowels:", count)
count_vowels()
# Example usag
# 9. Countdown: countdown

def countdown():
    n = int(input("Enter a number: "))
    for i in range(n, 0, -1):
        print(i)
countdown()


# 10. Guess the Number: guess_number_game

import random

def guess_number_game():
    number = random.randint(1, 100)
    guess = None
    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    print("Correct! The number was", number)
guess_number_game()
# Example usage

# 11. Factorial Calculation: calculate_factorial

def calculate_factorial():
    n = int(input("Enter a number: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial:", factorial)
calculate_factorial()
# Example usage

# 12. Fibonacci Sequence: fibonacci_sequence

def fibonacci_sequence():
    n = int(input("Enter the number of terms: "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
fibonacci_sequence()
# Example usage
# 13. Convert to Uppercase: to_uppercase

def to_uppercase():
    text = input("Enter a string: ")
    print("Uppercase string:", text.upper())
to_uppercase()
# Example usage

# 14. Calculate Square: square_number

def square_number():
    n = int(input("Enter a number: "))
    print("Square:", n ** 2)

# Example usage
square_number()
# 15. Check Palindrome: is_palindrome

def is_palindrome():
    text = input("Enter a string: ")
    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
is_palindrome()
# Example usage

# 16. Find Maximum: find_maximum

def find_maximum():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
    print("Maximum number:", max(numbers))
find_maximum()

# Example usage



