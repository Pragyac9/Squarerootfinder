import math


def main():
    # Get input from user
    num_str = input("Enter a number to find its square root: ")

    try:
        # Convert input string to float
        num = float(num_str)

        # Calculate square root
        sqrt_val = math.sqrt(num)

        # Display the result
        print(f"The square root of {num} is {sqrt_val}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
