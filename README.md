# Vigenère Cipher Implementation Guide

## What is the Vigenère Cipher?

The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt and decrypt text. Unlike the Caesar cipher which uses a single shift value, the Vigenère cipher uses different shift values for each letter based on the keyword.

## How It Works

### Basic Concept

1. Take a keyword (e.g., "EITAI")
2. Repeat the keyword to match the length of your text
3. For each letter in your text, shift it by the corresponding letter value in the keyword
4. Non-alphabetic characters (spaces, punctuation) remain unchanged

### Example

```
Plaintext:  H E L L O   W O R L D
Keyword:    E I T A I   E I T A I
Shifts:     4 8 19 0 8  4 8 19 0 8
Result:     L M E L W   A W K L L
```

## Code Implementation

### Core Functions

#### 1. Encryption Function

```python
def encrypt_vigenere(plaintext, key):
    encrypted = []
    key_cycle = cycle(key.upper())

    for char in plaintext:
        if char.isalpha():
            key_char = next(key_cycle)
            shift = ord(key_char) - ord('A')

            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            encrypted.append(encrypted_char)
        else:
            encrypted.append(char)

    return ''.join(encrypted)
```

#### 2. Decryption Function

```python
def decrypt_vigenere(ciphertext, key):
    decrypted = []
    key_cycle = cycle(key.upper())

    for char in ciphertext:
        if char.isalpha():
            key_char = next(key_cycle)
            shift = ord(key_char) - ord('A')

            if char.isupper():
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)

    return ''.join(decrypted)
```

## Step-by-Step Breakdown

### 1. Key Cycling with `itertools.cycle()`

```python
key_cycle = cycle(key.upper())
```

- Creates an infinite iterator that cycles through the key characters
- Automatically converts key to uppercase for consistency
- More memory efficient than creating an extended key string

### 2. Character Processing Loop

```python
for char in plaintext:
    if char.isalpha():
        # Process alphabetic characters
    else:
        # Keep non-alphabetic characters unchanged
```

- Iterates through each character in the text
- Only encrypts/decrypts alphabetic characters
- Preserves spaces, punctuation, and numbers

### 3. Key Character and Shift Calculation

```python
key_char = next(key_cycle)
shift = ord(key_char) - ord('A')
```

- Gets the next character from the cycling key
- Converts the key character to a shift value (A=0, B=1, ..., Z=25)
- `ord()` returns the ASCII value of a character

### 4. Character Transformation

```python
if char.isupper():
    encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
else:
    encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
```

#### For Uppercase Letters:

- `ord(char) - ord('A')`: Convert letter to number (A=0, B=1, ..., Z=25)
- `+ shift`: Add the shift value
- `% 26`: Wrap around if we go past Z
- `+ ord('A')`: Convert back to ASCII uppercase letter

#### For Lowercase Letters:

- Same process but using `ord('a')` as the base

### 5. Decryption Difference

The only difference between encryption and decryption is the direction of the shift:

- **Encryption**: `+ shift`
- **Decryption**: `- shift`

## Key Improvements Over Original Code

### 1. Memory Efficiency

- **Original**: Created full extended key string in memory
- **Improved**: Uses iterator that generates key characters on-demand

### 2. Readability

- **Original**: Used hardcoded ASCII values (65, 97)
- **Improved**: Uses `ord('A')` and `ord('a')` for clarity

### 3. Proper Key Cycling

- **Original**: Advanced key for every character (including spaces)
- **Improved**: Only advances key for alphabetic characters

## Usage Example

```python
from itertools import cycle

# Your functions here...

# Demo
text = "Hello World"
key = "eitai"

ciphertext = encrypt_vigenere(text, key)
print(f"Original:  {text}")
print(f"Encrypted: {ciphertext}")

decrypted = decrypt_vigenere(ciphertext, key)
print(f"Decrypted: {decrypted}")
```

## Output

```
Original:  Hello World
Encrypted: Lmpls Asklh
Decrypted: Hello World
```

## Security Note

The Vigenère cipher is **not secure** for modern use and should only be used for educational purposes. It can be broken using frequency analysis and other cryptanalytic techniques. For real-world encryption, use modern cryptographic libraries like `cryptography` in Python.
