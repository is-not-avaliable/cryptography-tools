import sys

def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''

    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 97)

    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 97)

    return plaintext

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("How to use: python3 vigenere.py [-E, -D] mayus(string keyword)")

    else:
        if sys.argv[1] == "-E":
            print(encrypt(sys.argv[2], sys.argv[3]))

        elif sys.argv[1] == "-D":
            print(decrypt(sys.argv[2], sys.argv[3]))

        else:
            print("How to use: python3 vigenere.py [-E, -D] mayus(string keyword)")
    