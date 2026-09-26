"""
Core base conversion module supporting standard bases (2, 8, 10, 16)
and arbitrary bases from 2 to 36.
"""

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert_base(value_str: str, from_base: int, to_base: int) -> str:
    """
    Converts a string representation of a number from one base to another.
    
    :param value_str: The number string to convert (e.g., "1010", "FF").
    :param from_base: The base of the input string (2 to 36).
    :param to_base: The target base (2 to 36).
    :return: String representation in the target base.
    """
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        raise ValueError("Bases must be between 2 and 36.")

    value_str = value_str.strip().upper()
    if not value_str:
        raise ValueError("Input string cannot be empty.")

    # Handle sign
    is_negative = value_str.startswith("-")
    if is_negative:
        value_str = value_str[1:]

    # Step 1: Convert input to decimal (Base-10) integer
    decimal_value = 0
    for char in value_str:
        if char not in DIGITS[:from_base]:
            raise ValueError(f"Invalid character '{char}' for base {from_base}.")
        decimal_value = decimal_value * from_base + DIGITS.index(char)

    if decimal_value == 0:
        return "0"

    # Step 2: Convert decimal integer to target base
    result_chars = []
    while decimal_value > 0:
        remainder = decimal_value % to_base
        result_chars.append(DIGITS[remainder])
        decimal_value //= to_base

    result = "".join(reversed(result_chars))
    return f"-{result}" if is_negative else result


if __name__ == "__main__":
    # Example usage
    val = "1A"  # 26 in Hex
    converted = convert_base(val, from_base=16, to_base=2)
    print(f"Hex {val} -> Binary {converted}")  # Output: 11010
