import string

def caesar_encode(message, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    return message.translate(translation_table)

def caesar_decode_simple(message, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(shifted_alphabet, alphabet)
    return message.translate(translation_table)

def caesar_decode_fancy(message, known_word):
    for shift in range(26):
        decoded_message = caesar_decode_simple(message, shift)
        if known_word in decoded_message:
            return decoded_message, shift
    return None, None

def vigenere_encode(message, keyword):
    keyword = keyword.lower()
    encoded_message = ""
    for i, char in enumerate(message):
        if char.isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('a')
            if char.isupper():
                encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encoded_char = char
        encoded_message += encoded_char
    return encoded_message

def vigenere_decode(message, keyword):
    keyword = keyword.lower()
    decoded_message = ""
    for i, char in enumerate(message):
        if char.isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('a')
            if char.isupper():
                decoded_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decoded_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decoded_char = char
        decoded_message += decoded_char
    return decoded_message

while True:
    cipher_choice = input("Enter cipher (Caesar or Vigenere): ").lower()
    if cipher_choice == "caesar":
        action_choice = input("Enter action (encode or decode): ").lower()
        if action_choice == "encode":
            message = input("Enter message: ")
            shift = int(input("Enter shift: "))
            encoded_message = caesar_encode(message, shift)
            print("Encoded message:", encoded_message)
        elif action_choice == "decode":
            decode_choice = input("Enter decode method (simple or fancy): ").lower()
            if decode_choice == "simple":
                message = input("Enter message: ")
                shift = int(input("Enter shift: "))
                decoded_message = caesar_decode_simple(message, shift)
                print("Decoded message:", decoded_message)
            elif decode_choice == "fancy":
                message = input("Enter message: ")
                known_word = input("Enter a word known to be in the message: ")
                decoded_message, shift = caesar_decode_fancy(message, known_word)
                if decoded_message is not None:
                    print("Decoded message:", decoded_message)
                    print("Shift used:", shift)
                else:
                    print("Could not find a valid shift.")
            else:
                print("Invalid decode method.")
        else:
            print("Invalid action.")
    elif cipher_choice == "vigenere":
        action_choice = input("Enter action (encode or decode): ").lower()
        if action_choice == "encode":
            message = input("Enter message: ")
            keyword = input("Enter keyword (lowercase, single word): ")
            encoded_message = vigenere_encode(message, keyword)
            print("Encoded message:", encoded_message)
        elif action_choice == "decode":
            decode_choice = input("Enter decode method (simple or fancy): ").lower()
            if decode_choice == "simple":
                message = input("Enter message: ")
                keyword = input("Enter keyword (lowercase, single word): ")
                decoded_message = vigenere_decode(message, keyword)
                print("Decoded message:", decoded_message)
            elif decode_choice == "fancy":
                print("Fancy decode is not supported for Vigenere.")
            else:
                print("Invalid decode method.")
        else:
            print("Invalid action.")
    else:
        print("Invalid cipher.")
