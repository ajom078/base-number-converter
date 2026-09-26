import pytest
from src.converter import convert_base


def test_standard_conversions():
    # Binary to Decimal
    assert convert_base("1010", 2, 10) == "10"
    # Hex to Binary
    assert convert_base("FF", 16, 2) == "11111111"
    # Octal to Hex
    assert convert_base("77", 8, 16) == "3F"


def test_zero_and_negative():
    assert convert_base("0", 10, 2) == "0"
    assert convert_base("-101", 2, 10) == "-5"


def test_invalid_input():
    with pytest.raises(ValueError):
        convert_base("102", 2, 10)  # '2' invalid for base 2
    with pytest.raises(ValueError):
        convert_base("A", 10, 16)  # 'A' invalid for base 10
