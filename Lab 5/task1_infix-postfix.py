# LAB ASSIGNMENT 5
# Task 1: Infix to Postfix Conversion


# --------------------------------
# Operator Stack
# --------------------------------

stack = []


# --------------------------------
# Check Operator
# --------------------------------

def is_operator(char):
    return char in "+-*/^"


# --------------------------------
# Operator Priority
# --------------------------------

def priority(operator):

    if operator == "^":
        return 3

    elif operator == "*" or operator == "/":
        return 2

    elif operator == "+" or operator == "-":
        return 1

    return 0


# --------------------------------
# Infix to Postfix
# --------------------------------

def infix_to_postfix(expression):

    stack = []
    postfix = ""

    for char in expression:

        # Ignore spaces
        if char == " ":
            continue

        # If character is an operand
        if char.isalnum():
            postfix += char

        # If opening bracket
        elif char == "(":
            stack.append(char)

        # If closing bracket
        elif char == ")":

            while len(stack) > 0 and stack[-1] != "(":
                postfix += stack.pop()

            # Remove opening bracket
            if len(stack) > 0:
                stack.pop()

        # If character is an operator
        elif is_operator(char):

            while (
                len(stack) > 0
                and stack[-1] != "("
                and priority(stack[-1]) >= priority(char)
            ):
                postfix += stack.pop()

            stack.append(char)

    # Pop remaining operators
    while len(stack) > 0:
        postfix += stack.pop()

    return postfix


# --------------------------------
# Main Program
# --------------------------------

expression = input("Enter a valid infix expression: ")

result = infix_to_postfix(expression)

print("Postfix expression:", result)