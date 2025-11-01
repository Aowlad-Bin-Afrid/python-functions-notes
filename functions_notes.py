
# ---------------------------------------------------------
# functions_notes.py
# ---------------------------------------------------------
# 📘  Functions & Modular Code (Notes)
# ---------------------------------------------------------

# 🔹 What is a Function?
# A function is a reusable block of code that performs a specific task.

# 🔹 Why use functions?
# - Makes code clean and organized
# - Avoids repetition
# - Easy to test and debug
# - Reusable in other programs

# ---------------------------------------------------------
# 📍 How to Define a Function:
# def function_name(parameters):
#     # code block
#     return result (optional)
#
# Example:
# def greet():
#     print("Hello, World!")

# ---------------------------------------------------------
# 📍 How to Call a Function:
# Just write its name followed by parentheses.
# Example:
# greet()

# ---------------------------------------------------------
# 📍 Function with Parameters:
# def greet_user(name):
#     print(f"Hello, {name}!")
#
# greet_user("Arafat")

# ---------------------------------------------------------
# 📍 Function with Return Value:
# def add(a, b):
#     return a + b
#
# result = add(5, 10)
# print(result)

# ---------------------------------------------------------
# 📍 Docstring (Documentation String):
# Used to describe what the function does.
#
# def multiply(a, b):
#     """Returns the product of two numbers."""
#     return a * b
#
# print(multiply(2, 3))

# ---------------------------------------------------------
# 📍 Local vs Global Variables:
# - Local: Defined inside a function
# - Global: Defined outside all functions
#
# x = 10   # global variable
#
# def show():
#     y = 5   # local variable
#     print(x + y)
#
# show()

# ---------------------------------------------------------
# 📍 Function with Loop Example:
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
# print(factorial(5))  # 120

# ---------------------------------------------------------
# 📍 Function Calling Another Function:
# def square(x):
#     return x * x
#
# def cube(x):
#     return x * square(x)
#
# print(cube(3))  # 27

# ---------------------------------------------------------
# ✅ Summary:
# - A function is defined using the `def` keyword.
# - Parameters go inside parentheses `()`.
# - The `return` keyword sends a value back to the caller.
# - To call a function, write its name followed by `()`.
# - Docstrings (`"""description"""`) describe what the function does.
