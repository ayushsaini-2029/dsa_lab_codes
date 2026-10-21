# LAB ASSIGNMENT 5
# Task 2: Postfix Expression Evaluation


# --------------------------------
# Postfix Evaluation
# --------------------------------

def evaluate_postfix(expression):

    stack = []

    for char in expression:

        # Ignore spaces
        if char == " ":
            continue

        # If character is a number
        if char.isdigit():

            stack.append(int(char))

        # If character is an operator
        elif char in "+-*/":

            # Remove two operands
            right = stack.pop()
            left = stack.pop()

            # Perform operation
            if char == "+":
                result = left + right

            elif char == "-":
                result = left - right

            elif char == "*":
                result = left * right

            elif char == "/":
                result = left / right

            # Put result back into stack
            stack.append(result)

    # Final result
    return stack.pop()


# --------------------------------
# Main Program
# --------------------------------

expression = input("Enter a valid postfix expression: ")

result = evaluate_postfix(expression)

print("Final result:", result)