alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # if direction == "encode":
    #     def encrypt(plaintext, shift_amount):
    #         cipher_text = ""
    #         for letter in plaintext:
    #             position = alphabet.index(letter)
    #             new_position = position + shift_amount
    #             new_letter = alphabet[new_position]
    #             cipher_text += new_letter
    #         print(f"Your encrypted word is {cipher_text}")
    #     encrypt(plaintext=text,shift_amount=shift)
    # elif direction == "decode":
    #     def decrypt(plaintext, shift_amount):
    #         cipher_text = ""
    #         for letter in plaintext:
    #             position = alphabet.index(letter)
    #             new_position = position - shift_amount
    #             new_letter = alphabet[new_position]
    #             cipher_text += new_letter
    #         print(f"Your decyrypted word is {cipher_text}")
    #     decrypt(plaintext=text,shift_amount=shift)
    shift = shift % 26

    def Ceaser(text,shift,direction):
        new_text = ""
        if direction == "decode":
            shift *= -1
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                new_text += alphabet[new_position]
            else:
                new_text += char
        print(f"Your {direction}d word is {new_text}")
    Ceaser(text=text,shift=shift,direction=direction)

    result = input("Do you want to continue? \n")
    if result == "no":
        should_continue = False
        print("Goodbye")
