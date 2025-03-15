def convert_base(n, from_base, to_base):
    """Converts a number from one base to another."""

    if not isinstance(n, int):
        raise TypeError("Input number must be an integer.")

    if not isinstance(from_base, int) or from_base < 2:
        raise ValueError("From base must be an integer >= 2.")

    if not isinstance(to_base, int) or to_base < 2:
        raise ValueError("To base must be an integer >= 2.")

    if n == 0:
        return "0"

    # Convert from 'from_base' to base 10
    decimal_value = 0
    power = 0
    while n > 0:
        digit = n % 10  # Assuming input number is represented in base 10 digits
        if digit >= from_base:
            raise ValueError(f"Digit {digit} is not valid for base {from_base}")
        decimal_value += digit * (from_base ** power)
        n //= 10
        power += 1

    # Convert from base 10 to 'to_base'
    result = ""
    while decimal_value > 0:
        remainder = decimal_value % to_base
        if remainder < 10:
           result = str(remainder) + result
        else:
           result = chr(ord('A') + remainder - 10) + result
        decimal_value //= to_base

    return result

def main():
    n = int(input("Input number to convert: "))
    f = int(input("Input base of this number: "))
    t = int(input("Input base to convert to: "))

    try:
        converted = convert_base(n, f, t)
        print(converted)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

#main()
if __name__ == "__main__":
    main()
