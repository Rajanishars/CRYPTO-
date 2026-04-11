# --- Helper Functions ---
def xor_bits(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result

def permute(bits, table):
    result = ""
    for position in table:
        result += bits[position - 1]
    return result

# --- DES Round 1 ---
def run_des():
    print("\n[DES Round 1]")
    pt = input("Enter 8-bit Plaintext (e.g. 10101010): ")
    key = input("Enter 10-bit Key (e.g. 1111100000): ")

    # User-defined tables (space-separated)
    p10 = [int(x) for x in input("Enter P10 (10 values): ").split()]
    p8  = [int(x) for x in input("Enter P8 (8 values): ").split()]
    ip  = [int(x) for x in input("Enter IP (8 values): ").split()]
    ep  = [int(x) for x in input("Enter EP (8 values): ").split()]

    # Key Generation (Shift)
    k_p10 = permute(key, p10)
    left_part = k_p10[1:5] + k_p10[0]  # Left shift 1
    right_part = k_p10[6:10] + k_p10[5] # Left shift 1
    k1 = permute(left_part + right_part, p8)
    print("Round 1 Key (K1):", k1)

    # Round 1 Steps
    pt_ip = permute(pt, ip)
    L0, R0 = pt_ip[:4], pt_ip[4:]

    expanded_R0 = permute(R0, ep)
    xor_result = xor_bits(expanded_R0, k1)

    print("After IP:", pt_ip)
    print("XOR Step:", xor_result)
    print("Final Round 1 Output (L1 R1):", R0 + xor_result[:4])

# --- AES Key Expansion (Round 1) ---
def run_aes():
    print("\n[AES Key Expansion]")
    # Simplified: Using integers to avoid hex/byte complexity
    w0 = [int(x, 16) for x in input("Enter W0 (4 hex bytes e.g. 2b 7e 15 16): ").split()]
    w3 = [int(x, 16) for x in input("Enter W3 (4 hex bytes e.g. 09 cf 4f 3c): ").split()]

    # 1. Rotate (RotWord)
    rot = [w3[1], w3[2], w3[3], w3[0]]
    print("Step 1 (Rotate):", rot)

    # 2. Simple Substitution (XOR 1 for demo)
    sub = []
    for byte in rot:
        sub.append(byte ^ 0x63)
    print("Step 2 (Substitute):", sub)

    # 3. XOR with W0 and Rcon (0x01)
    w4 = []
    rcon = [1, 0, 0, 0]
    for i in range(4):
        val = sub[i] ^ rcon[i] ^ w0[i]
        w4.append(val)

    print("Final W4 (Hex):", [hex(x) for x in w4])

# --- Main Program ---
choice = input("Type AES or DES: ").upper()
if choice == "DES":
    run_des()
else:
    run_aes()
