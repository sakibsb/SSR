import math
import random

p, q = 101, 103
n, phi = p * q, (p - 1) * (q - 1)
e = 7
d = next(d for d in range(1, phi) if (d * e) % phi == 1)

encrypt = lambda m: pow(m, e, n)
decrypt = lambda c: pow(c, d, n)

# Blinding Phase
def blind_message(msg):
    r = random.choice([r for r in range(2, n) if math.gcd(r, n) == 1])
    return (msg * pow(r, e, n)) % n, r 

# Signing Phase
def sign_blinded_message(blinded):
    return decrypt(blinded)

# Unblinding Phase
def unblind_message(signed, r):
    return (signed * pow(r, -1, n)) % n

# Verification
def verify_signature(unblinded_sig, original_msg):
    return encrypt(unblinded_sig) == original_msg

# Main program
if __name__ == "__main__":
    message = input("Enter a message to blind and sign: ")
    message_int = sum(ord(c) for c in message)

    # Blinding Phase
    blinded, r = blind_message(message_int)
    print(f"Blinded message: {blinded}") 
    
    signed_blinded = sign_blinded_message(blinded)
    print(f"Signed blinded message: {signed_blinded}")  

    # Unblinding Phase
    unblinded_sig = unblind_message(signed_blinded, r)
    print(f"Unblinded signature: {unblinded_sig}") 
   
    print("Signature is valid!" if verify_signature(unblinded_sig, message_int) else "Signature is invalid!")