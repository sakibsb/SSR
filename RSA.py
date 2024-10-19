p, q = 101, 103
n, phi = p * q, (p - 1) * (q - 1)
e = 7  # Define e first
d = next(d for d in range(1, phi) if (d * e) % phi == 1)

encrypt = lambda m: pow(m, e, n)
decrypt = lambda c: pow(c, d, n)
encoder = lambda msg: [encrypt(ord(c)) for c in msg]
decoder = lambda enc: "".join(chr(decrypt(c)) for c in enc)

message = input("Enter the message: ")
encrypted = encoder(message)
print("\nEncrypted:", encrypted)
print("Decrypted:", decoder(encrypted))