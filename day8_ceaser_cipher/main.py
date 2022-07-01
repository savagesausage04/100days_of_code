from art import logo
print(logo)

def cipher(text, shift, direction):
    ending_text = ''
    for character in text:
        if character in alphabet:
            position = alphabet.index(character)
            if direction == "encode":
                new_position = position + shift
            elif direction == "decode":
                new_position = position - shift
            new_letter = alphabet[new_position]
            ending_text += new_letter
        else:
            ending_text += character
    print(f"The {direction}d text is {ending_text}")

will_continue = True
while will_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    #shift number >26 wont break code

    cipher(text, shift, direction)

    play_again = input("Do you want to continue? Yes or No.\n")
    if play_again.lower() == "no":
        will_continue = False
        print("Take care.")

