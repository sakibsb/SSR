import random
import math

# Function to calculate gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to generate a valid blinding factor
def generate_blinding_factor(n):
    r = random.randint(2, n - 1)
    while gcd(r, n) != 1:  # Ensure r is coprime to n
        r = random.randint(2, n - 1)
    return r

# Function to find the private key 'd'
def find_private_key(e, phi):
    d = 1
    while (d * e) % phi != 1:
        d += 1
    return d

# Function to encrypt (RSA)
def encrypt(message, e, n):
    return pow(message, e, n)

# Function to decrypt (RSA)
def decrypt(encrypted_message, d, n):
    return pow(encrypted_message, d, n)

# Blinding the message
def blind_message(m, e, n, a1, a2, r1, r2):
    alpha1 = (pow(r1, e, n) * pow(m, a1, n)) % n
    alpha2 = (pow(r2, e, n) * pow(m, a2, n)) % n
    return alpha1, alpha2

# Signing the blinded message
def sign_message(alpha1, alpha2, d, b1, b2, n):
    t1 = pow(alpha1, b1 * d, n)
    t2 = pow(alpha2, b2 * d, n)
    return t1, t2

# Unblinding the signed message
def unblind_message(t1, t2, r1, r2, b1, b2, w, t, n):
    s1 = (t1 * pow(r1, -b1, n)) % n  # Use r1^(-b1)
    s2 = (t2 * pow(r2, -b2, n)) % n  # Use r2^(-b2)
    s = (pow(s1, w, n) * pow(s2, t, n)) % n  # Final unblinded signature
    return s, s1, s2

# Main program for Hwang's Blind Signature Scheme
if __name__ == "__main__":
    # Step 1: Choose two small prime numbers
    p, q = 101, 103
    n = p * q
    phi = (p - 1) * (q - 1)

    # Step 2: Choose a public key 'e' (must be coprime with phi)
    e = 7
    d = find_private_key(e, phi)  # Find private key 'd'

    # Input from the user (original message)
    message = input("Enter a message to blind and sign: ")
    m = sum(ord(c) for c in message)  # Convert message to an integer

    # Step 3: Generate blinding factors and random numbers
    r1 = generate_blinding_factor(n)
    r2 = generate_blinding_factor(n)  # Second blinding factor
    a1, a2 = random.randint(1, n - 1), random.randint(1, n - 1)
    b1, b2 = random.randint(1, n - 1), random.randint(1, n - 1)  # Random signing numbers

    # Step 4: Blinding the message
    alpha1, alpha2 = blind_message(m, e, n, a1, a2, r1, r2)
    print(f"Blinded message (alpha1): {alpha1}")
    print(f"Blinded message (alpha2): {alpha2}")

    # Step 5: Signer signs the blinded messages
    t1, t2 = sign_message(alpha1, alpha2, d, b1, b2, n)
    print(f"Signed blinded message (t1): {t1}")
    print(f"Signed blinded message (t2): {t2}")

    # Step 6: Unblind the signed messages
    w = random.randint(1, n - 1)  # Generate w for unblinding
    t = random.randint(1, n - 1)  # Generate t for unblinding
    s, s1, s2 = unblind_message(t1, t2, r1, r2, b1, b2, w, t, n)
    print(f"Final unblinded signature (s): {s}")
    print(f"Unblinded signature (s1): {s1}")
    print(f"Unblinded signature (s2): {s2}")

    # Step 7: Verify the signatures using the public key
    if encrypt(s, e, n) == m:
        print("Final signature s is valid!")
    else:
        print("Final signature s is invalid!")
