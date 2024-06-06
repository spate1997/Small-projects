def caesar_cipher_encode(text, key):
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char  # Non-alphabetic characters are added as is
    return result

def caesar_cipher_decode(text, key):
    return caesar_cipher_encode(text, -key)

# Example usage:
encoded = caesar_cipher_encode("HI", 2)
decoded = caesar_cipher_decode(encoded, 2)

print(f"Encoded: {encoded}")  # Output: JK
print(f"Decoded: {decoded}")  # Output: HI
