# input_handler.py

from constants import VALID_CHOICES

def get_input(prompt):
    """Get input from the user."""
    return input(prompt)

def get_choice():
    """Get the user's choice of action."""
    while True:
        try:
            choice = int(get_input('Enter:\n1 - Change format\n2 - Trim\n'))
            if choice in VALID_CHOICES:
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")
