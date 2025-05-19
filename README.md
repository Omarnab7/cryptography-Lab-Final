# Save the generated Markdown content for MSSP.py to a .md file
mssp_md_content = """\
# MSSP Cipher Decoder

This script decodes a special type of numeric cipher text using a method based on subset rotation and shared integer values. It performs several validations and analyzes which integers appear in every subset combination.

---

## Features

- Validates the cipher text against custom rules:
  - Must be all digits
  - Must be divisible by the number of subsets
  - Each subset's length must be divisible by a specified digit count
- Splits the cipher into equal subsets
- Breaks each subset into integers of a specific digit length
- Calculates all possible sums of combinations
- Identifies common integers across all subsets

---

## Custom Exceptions

The script defines custom exceptions for precise error handling:

- `CipherTextError`: Base class for cipher text-related errors.
- `NonDigitInputError`: Raised if the cipher contains non-digit characters.
- `LengthNotDivisibleError`: Raised if total cipher length isn’t divisible by the number of subsets.
- `SubsetDivisibilityError`: Raised if subsets can't be evenly broken into groups of the required digit length.

---

## Main Functions

### `validate_cipher(ciphertext, num_subsets, digit_divisor)`

Validates the format and structure of the cipher text.

### `break_subset_into_ints(subset, digit_divisor)`

Splits a numeric string into integers of a fixed digit length.

### `get_all_subset_sums(int_list)`

Generates all unique subset sums from a list of integers.

### `mssp_decode(ciphertext, num_subsets, digit_divisor)`

Decodes the cipher text to find the shared integer across all subsets.

---

## Example Usage

```python
cipher = "55495458205016966826278532461565"
num_subsets = 5
digit_divisor = 3

plaintext = mssp_decode(cipher, num_subsets, digit_divisor)
print(f"Decoded shared number: {plaintext}")
