def simple_fixed_length_hash(message, bit_size=32):
    hash_value = 0
    for char in message:
        hash_value = ((hash_value << 5) - hash_value + ord(char)) & ((1 << bit_size) - 1)
    return f"{hash_value:0{bit_size // 4}x}"

if __name__ == "__main__":
    message = input("Enter a message to hash: ")
    print(f"Hashed value (32-bit): {simple_fixed_length_hash(message)}")