# Caesar cipher using python pract-1 19/1/23

# For ecrypting the text
def encrypt(text,s):
    ciphered_text = ""
   # transverse the plain text
    for i in range(len(text)):
        char = text[i]

        # Encrypt space as space
        if (char == " "):
            ciphered_text += " "
        # Encrypt uppercase characters in plain text
        elif (char.isupper()):
            ciphered_text += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        elif (char.isalpha()):
            ciphered_text += chr((ord(char) + s - 97) % 26 + 97)
        else:
            ciphered_text += char

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
