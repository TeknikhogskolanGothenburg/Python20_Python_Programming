encipherkey = {'a' : 'd' ,'b' : 'e' ,'c' : 'f' ,'d' : 'g' ,'e' : 'h' ,'f' : 'i' ,'g' : 'j' ,'h' : 'k' ,
               'i' : 'l' ,'j' : 'm' ,'k' : 'n' ,'l' : 'o' ,'m' : 'p' ,'n' : 'q' ,'o' : 'r' ,'p' : 's' ,
               'q' : 't' ,'r' : 'u' ,'s' : 'v' ,'t' : 'w' ,'u' : 'x' ,'v' : 'y' ,'w' : 'z' ,'x' : 'a' ,
               'y' : 'b' ,'z' : 'c' ,'A' : 'D' ,'B' : 'E' ,'C' : 'F' ,'D' : 'G' ,'E' : 'H' ,'F' : 'I' ,
               'G' : 'J' ,'H' : 'K' ,'I' : 'L' ,'J' : 'M' ,'K' : 'N' ,'L' : 'O' ,'M' : 'P' ,'N' : 'Q' ,
               'O' : 'R' ,'P' : 'S' ,'Q' : 'T' ,'R' : 'U' ,'S' : 'V' ,'T' : 'W' ,'U' : 'X' ,'V' : 'Y' ,
               'W' : 'Z' ,'X' : 'A' ,'Y' : 'B' ,'Z' : 'C'  }

decipherkey = {'a' : 'x' ,'b' : 'y' ,'c' : 'z' ,'d' : 'a' ,'e' : 'b' ,'f' : 'c' ,'g' : 'd' ,'h' : 'e' ,
               'i' : 'f' ,'j' : 'g' ,'k' : 'h' ,'l' : 'i' ,'m' : 'j' ,'n' : 'k' ,'o' : 'l' ,'p' : 'm' ,
               'q' : 'n' ,'r' : 'o' ,'s' : 'p' ,'t' : 'q' ,'u' : 'r' ,'v' : 's' ,'w' : 't' ,'x' : 'u' ,
               'y' : 'v' ,'z' : 'w' ,'A' : 'X' ,'B' : 'Y' ,'C' : 'Z' ,'D' : 'A' ,'E' : 'B' ,'F' : 'C' ,
               'G' : 'D' ,'H' : 'E' ,'I' : 'F' ,'J' : 'G' ,'K' : 'H' ,'L' : 'I' ,'M' : 'J' ,'N' : 'K' ,
               'O' : 'L' ,'P' : 'M' ,'Q' : 'N' ,'R' : 'O' ,'S' : 'P' ,'T' : 'Q' ,'U' : 'R' ,'V' : 'S' ,
               'W' : 'T' ,'X' : 'U' ,'Y' : 'V' ,'Z' : 'W'  }

def encipher(message):
    cipher_message = ""
    for letter in message:
        if letter.isalpha():
            cipher_message += encipherkey[letter]
        else:
            cipher_message += letter
    return cipher_message


def decipher(cipher_message):
    clear_message = ""
    for letter in cipher_message:
        if letter.isalpha():
            clear_message += decipherkey[letter]
        else:
            clear_message += letter
    return clear_message


def main():
    message = "Hello there!"
    cipher_message = encipher(message)
    print(cipher_message)

    clear_message = decipher(cipher_message)
    print(clear_message)


if __name__ == '__main__':
    main()
