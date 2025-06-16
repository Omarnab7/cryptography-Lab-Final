import enchant  # type: ignore

def encrypt_caesar_cipher(data: str, nkey: int = 2) -> str:
    if not data.replace(' ', '').isalpha():
        raise ValueError("Bruhhhh, pls use string with alphabetic only duh")
    res = []
    for char in data.lower():  # Process each character
        if char == ' ':
            res.append(' ')
            continue

        shifted = ord(char) - ord('a')  # Convert to 0-25 position
        shifted = (shifted + nkey) % 26  # Apply Caesar shift
        encrypted_char = chr(shifted + ord('a'))  # Back to Unicode
        res.append(encrypted_char)

    return ''.join(res)  # Return as a string

def decrypt_caesar_cipher(ct):
    d = enchant.Dict("en_US")
    chosen_text, chosen_index = None, None
    permutes = []
    for i in range(26):
        supposed_data = encrypt_caesar_cipher(ct, -i)
        permutes.append(supposed_data)

        # For documentation, the following code just makes sure
        # atleast two words are english to negate false detections
        sums = sum([int(d.check(word)) for word in supposed_data.split()])
        if sums > 2:
            chosen_text = supposed_data
            chosen_index = -i
    return permutes, chosen_text, chosen_index


