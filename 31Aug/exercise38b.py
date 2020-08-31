def create_encipher_key(rot):
    encipherkey = {}
    for i in range(65, 91):
        if i < 91-rot:
            encipherkey[chr(i)] = chr(i+rot)
        else:
            encipherkey[chr(i)] = chr(i-26+rot)

    for i in range(97, 123):
        if i < 123-rot:
            encipherkey[chr(i)] = chr(i+rot)
        else:
            encipherkey[chr(i)] = chr(i-26+rot)
    return encipherkey

def create_decipher_key(rot):
    decipherkey = {}
    for i in range(65, 91):
        if i >= 65 + rot:
            decipherkey[chr(i)] = chr(i-rot)
        else:
            decipherkey[chr(i)] = chr(i+26-rot)

    for i in range(97, 123):
        if i >= 97 + rot:
            decipherkey[chr(i)] = chr(i-rot)
        else:
            decipherkey[chr(i)] = chr(i+26-rot)
    return decipherkey

def encipher(message, encipherkey):
    cipher_message = ""
    for letter in message:
        if letter.isalpha():
            cipher_message += encipherkey[letter]
        else:
            cipher_message += letter
    return cipher_message


def decipher(cipher_message, decipherkey):
    clear_message = ""
    for letter in cipher_message:
        if letter.isalpha():
            clear_message += decipherkey[letter]
        else:
            clear_message += letter
    return clear_message


def main():
    encipherkey = create_encipher_key(9)
    decipherkey = create_decipher_key(9)
    message = "Hello there!"
    cipher_message = encipher(message, encipherkey)
    print(cipher_message)

    clear_message = decipher(cipher_message, decipherkey)
    print(clear_message)





if __name__ == '__main__':
    main()
