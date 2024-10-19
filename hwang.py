import math
import random

# Initialization
p, q = 101, 103
n, phi = p * q, (p - 1) * (q - 1)
e = 7
d = next(d for d in range(1, phi) if (d * e) % phi == 1)

# RSA Encryption and Decryption Functions
encrypt = lambda m: pow(m, e, n)
decrypt = lambda c: pow(c, d, n)

# Hwang’s additional security link
def hwang_security_link(user_id, msg, signer_secret):
    return (user_id + msg + signer_secret) % signer_secret

# Blinding Phase
def blind_message(msg):
    r = random.choice([r for r in range(2, n) if math.gcd(r, n) == 1])
    return (msg * pow(r, e, n)) % n, r

# Unblinding Phase
def unblind_message(signed, r):
    return (signed * pow(r, -1, n)) % n

# Main program
if __name__ == "__main__":
    message = input("Enter a message to blind and sign: ")
    user_id = int(input("Enter your user ID (as an integer): "))
    message_int = sum(ord(c) for c in message)

    signer_secret = random.randint(1000, 9999)
    secure_link_message = hwang_security_link(user_id, message_int, signer_secret)
    
    blinded_message, r = blind_message(secure_link_message)
    signed_blinded_message = decrypt(blinded_message)
    unblinded_signature = unblind_message(signed_blinded_message, r)

    # Verification Phase
    print(
        "Signature is valid!" if encrypt(unblinded_signature) == secure_link_message
        else "Signature is invalid!"
    )