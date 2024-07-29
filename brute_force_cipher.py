# ------------------------------------------------------CAESAR CIPHER PROJECT 4---------------------------------------------------------------------------
alphabet = ['a','b','c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v', 'w','x','y','z']

def Encryption(plain_text, shift_keys):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_keys) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char  # Non-alphabet characters remain unchanged
    print(f"The Cipher Text is: {cipher_text}")
    return cipher_text

def Decryption(cipher_text, shift_keys):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_keys) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char  # Non-alphabet characters remain unchanged
    print(f"The Plain Text is: {plain_text}")
    return plain_text

def brute_force_decrypt(encrypted_text):
    print("Starting brute force decryption...")
    for shift in range(1, 26):
        decrypted_text = Decryption(cipher_text=encrypted_text, shift_keys=shift)
        print(f"Shift {shift}: {decrypted_text}")

print("WELCOME TO CIPHER TEXT")
wanna_end = False
while not wanna_end:
    what_to_do = input("Type 'encrypt' for Encryption, and 'decrypt' for Decryption, or 'brute' for Brute Force Decryption: \n").lower()
    text = input("Type Message: \n").lower()
    
    if what_to_do in ["encrypt", "decrypt"]:
        shift = int(input("Enter Number of Shifts Keys: \n"))
    
    if what_to_do == "encrypt":
        Encryption(plain_text=text, shift_keys=shift)
    elif what_to_do == "decrypt":
        Decryption(cipher_text=text, shift_keys=shift)
    elif what_to_do == "brute":
        brute_force_decrypt(encrypted_text=text)
    else:
        print("Invalid option. Please type 'encrypt', 'decrypt', or 'brute'.")

    play_again = input("Type 'yes' to continue - Type 'no' to exit. \n").lower()
    if play_again == 'no':
        wanna_end = True
        print("Good Bye, Have a Nice Day!")

# Example usage for brute force decryption can be tested within the interactive part by selecting 'brute force' as the action.
