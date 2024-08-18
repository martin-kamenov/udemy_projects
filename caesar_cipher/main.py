from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text: str, shift_amount: int, encode_or_decode: str):
    output_text = ""

    if encode_or_decode == 'decode':
        shift_amount *= -1

    for char in original_text:
        if char not in alphabet:
            output_text += char
        else:
            shifted_char = alphabet.index(char) + shift_amount
            shifted_char %= len(alphabet)
            output_text += alphabet[shifted_char]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == 'no':
        should_continue = False
        print("Goodbye!")