import math

def get_mod_inverse(e, phi):
    # Manually find d such that (d * e) % phi == 1
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def run_rsa():
    print("--- RSA Algorithm ---")
    p = int(input("Enter Prime p: "))
    q = int(input("Enter Prime q: "))
    msg = int(input("Enter numeric message: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    # 1. Find 'e' where gcd(e, phi) == 1
    e = 2
    while e < phi:
        if math.gcd(e, phi) == 1:
            break
        e += 1

    # 2. Use the manual function to find 'd'
    d = get_mod_inverse(e, phi)

    if d is None:
        print("Error: Could not find modular inverse. Check your primes.")
        return

    # 3. Encryption / Decryption
    cipher = pow(msg, e, n)
    decrypted = pow(cipher, d, n)

    print(f"\n--- Results ---")
    print(f"n: {n}, phi: {phi}")
    print(f"Public Key (e): {e}")
    print(f"Private Key (d): {d}")
    print(f"Encrypted Cipher: {cipher}")
    print(f"Decrypted Message: {decrypted}")


def run_diffie_hellman():
    print("--- Diffie-Hellman Key Exchange ---")
    p = int(input("Enter Prime (p): "))
    g = int(input("Enter Primitive Root (g): "))
    a = int(input("Alice's Private Key: "))
    b = int(input("Bob's Private Key: "))

    # Generate Public Keys
    A = pow(g, a, p)
    B = pow(g, b, p)

    # Compute Shared Secrets
    alice_shared = pow(B, a, p)
    bob_shared = pow(A, b, p)

    print(f"\nAlice's Public Key: {A}")
    print(f"Bob's Public Key: {B}")
    print(f"Resulting Shared Secret: {alice_shared}")

run_diffie_hellman()

if __name__ == "__main__":
    run_rsa()
