key = 21

with open('flag.txt', 'r') as file:
    plaintext = file.read().strip()

ciphertext = ''.join(
    chr((ord(c) - ord('a') - key) % 26 + ord('a')) if 'a' <= c <= 'z' else c
    for c in plaintext
)

with open('ciphertext.txt', 'w+') as file:
    file.write(ciphertext)
