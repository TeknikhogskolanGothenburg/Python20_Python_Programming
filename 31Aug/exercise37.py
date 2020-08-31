key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

def encode(text):
    encoded_text = ""
    for letter in text:
        if letter.isalpha():
            encoded_text += key[letter]
        else:
            encoded_text += letter
    return encoded_text

def main():
    cipher = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
    result = encode(cipher)

    print(result)

    my_cipher = encode("This is my secret message!")
    print(my_cipher)
    my_clear_text = encode(my_cipher)
    print(my_clear_text)



if __name__ == '__main__':
    main()
