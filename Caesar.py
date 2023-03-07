import random
import course



should_end = True
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount):
    cipher_text = ""
    if direction == 'decode':
        shift_amount *= -1
    for char in plain_text:
        if char in letters:
            length = letters.index(char)
            actual_length = length + shift_amount
            cipher_text += letters[actual_length]
        else: cipher_text += char
    print(f"The {direction}d text is {cipher_text}")

from art import logo
print(logo)


while should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    statement = input('Type your message:\n').lower()
    shift = int(input("How many letters would you like to shift by?\n"))
    #if you shift by 26 it does nothing
    shift = shift % 26

    caesar(plain_text = statement, shift_amount = shift)

    restart = input('Type "yes" if you want to repeat the program. Otherwise type "no".\n')
    if restart == "no":
        should_end = False
        print('さよなら')
