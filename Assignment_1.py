import string

def encrypt_char(c, n, m): 
    if c.islower():
        if c <= 'm':
            return chr((ord(c) - ord('a') + n * m) % 26 + ord('a'))
        else:
            return chr((ord(c) - ord('a') - (n + m)) % 26 + ord('a'))
    elif c.isupper():
        if c <= 'M':
            return chr((ord(c) - ord('A') - n) % 26 + ord('A'))
        else:
            return chr((ord(c) - ord('A') + m * m) % 26 + ord('A'))
    else:
        return c  # Keep special characters and digits unchanged

def decrypt_char(c, n, m):
    if c.islower():
        if c <= 'm':
            return chr((ord(c) - ord('a') - n * m) % 26 + ord('a'))
        else:
            return chr((ord(c) - ord('a') + (n + m)) % 26 + ord('a'))
    elif c.isupper():
        if c <= 'M':
            return chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        else:
            return chr((ord(c) - ord('A') - m * m) % 26 + ord('A'))
    else:
        return c

def encrypt_text(text, n, m):
    return ''.join(encrypt_char(c, n, m) for c in text)

def decrypt_text(text, n, m):
    return ''.join(decrypt_char(c, n, m) for c in text)

def check_correctness(original, decrypted):
    return original == decrypted

def main():
    n = int(input("Enter value of n: "))
    m = int(input("Enter value of m: "))

    with open("raw_text.txt", "r", ) as file:
        raw_text = file.read()

    encrypted_text = encrypt_text(raw_text, n, m)
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    # Decryption and verification
    decrypted_text = decrypt_text(encrypted_text, n, m)
    is_correct = check_correctness(raw_text, decrypted_text)

    print("Encryption and decryption completed.")
    print("Decryption correct:", is_correct)

if __name__ == "__main__":
    main()