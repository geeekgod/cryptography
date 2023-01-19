# Caesar cipher using python pract-1 19/1/23

# For ecrypting the text
def encrypt(text,s):
    ciphered_text = ""
   # transverse the plain text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            ciphered_text += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            ciphered_text += chr((ord(char) + s - 97) % 26 + 97)

    return ciphered_text

# # For decrypting the text
def decrypt(cipher, s):
    deciphered_text = encrypt(cipher, 26-s)
    return deciphered_text

text = input("Enter the text: ")
shift = int(input("Enter the shift pattern: "))
ciphered = encrypt(text, shift)
deciphered = decrypt(ciphered, shift)

print("Cipher text: " + ciphered)
print("Decipher text: " + deciphered)
