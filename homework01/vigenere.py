def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    keyword_length = len(keyword)
    keyword_as_int = [ord(i) for i in keyword]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + keyword_as_int[i % keyword_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    keyword_length = len(keyword)
    keyword_as_int = [ord(i) for i in keyword]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - keyword_as_int[i % keyword_length]) % 26
        plaintext += chr(value + 65)
    return plaintext