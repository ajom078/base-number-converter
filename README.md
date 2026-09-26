# Base Number Converter

A lightweight, flexible Python library for converting numbers between arbitrary bases (from Base-2 to Base-36), including standard bases like Binary, Octal, Decimal, and Hexadecimal.

## Features

- Converts between any base from **2** to **36**.
- Supports negative numbers and standard alphanumeric representations (`A-Z` for values 10–35).
- Clean unit testing suite using `pytest`.

## Quick Start

### Prerequisites
- Python 3.8 or higher

### Usage

```python
from src.converter import convert_base

# Convert Hexadecimal '1A' to Binary
binary_val = convert_base("1A", from_base=16, to_base=2)
print(binary_val)  # Output: '11010'

# Convert Decimal '255' to Hexadecimal
hex_val = convert_base("255", from_base=10, to_base=16)
print(hex_val)  # Output: 'FF'
