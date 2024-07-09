def caesar_cipher_encode(text, key):
    result = ""
    # Iterate over each character in the input text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the base ASCII value depending on whether the letter is upper or lower case
            shift = ord('A') if char.isupper() else ord('a')
            # Encode the character by shifting it by the key value within the alphabet
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            # Non-alphabetic characters are added to the result without modification
            result += char
    return result

def caesar_cipher_decode(text, key):
    # Decoding is the same as encoding but using the negative of the key
    return caesar_cipher_encode(text, -key)

# Example usage:
encoded = caesar_cipher_encode("HI", 2)  # Encodes "HI" with a key of 2
decoded = caesar_cipher_decode(encoded, 2)  # Decodes the result back to "HI"

print(f"Encoded: {encoded}")  # Output: JK
print(f"Decoded: {decoded}")  # Output: HI


