def generate_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # Remove duplicates and merge J into I
    unique_key = ""
    for char in (key.upper().replace('J', 'I') + alphabet):
        if char.isalpha() and char not in unique_key:
            unique_key += char

    matrix = [list(unique_key[i:i+5]) for i in range(0, 25, 5)]
    return matrix

def print_matrix(matrix):
    print("\n--- 5x5 Key Matrix ---")
    for row in matrix:
        print("  ".join(row))
    print("----------------------")

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)
    return None

def prepare_text(text, is_encrypt):
    text = "".join(filter(str.isalpha, text.upper())).replace('J', 'I')
    if not is_encrypt: return text

    prepared = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if (i + 1) < len(text) else 'X'
        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2
    if len(prepared) % 2 != 0: prepared += 'X'
    return prepared

def process_logic(text, matrix, is_encrypt):
    result = ""
    mode_label = "Encrypting" if is_encrypt else "Decrypting"
    print(f"\n--- Intermediate {mode_label} Steps ---")

    for i in range(0, len(text), 2):
        pair = text[i:i+2]
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])

        char1, char2 = "", ""
        if r1 == r2: # Same row
            shift = 1 if is_encrypt else -1
            char1 = matrix[r1][(c1 + shift) % 5]
            char2 = matrix[r2][(c2 + shift) % 5]
            rule = "Same Row (Shift)"
        elif c1 == c2: # Same column
            shift = 1 if is_encrypt else -1
            char1 = matrix[(r1 + shift) % 5][c1]
            char2 = matrix[(r2 + shift) % 5][c2]
            rule = "Same Col (Shift)"
        else: # Rectangle
            char1 = matrix[r1][c2]
            char2 = matrix[r2][c1]
            rule = "Rectangle (Swap)"

        result += char1 + char2
        print(f"Pair: {pair} -> {char1}{char2} | Rule: {rule}")

    return result

# --- Main Execution ---
user_key = input("Enter Secret Key: ")
user_msg = input("Enter Message: ")

# 1. Generate and Display Matrix
matrix = generate_matrix(user_key)
print_matrix(matrix)

# 2. Encryption
prep_enc = prepare_text(user_msg, True)
cipher_text = process_logic(prep_enc, matrix, True)
print(f"\nFINAL ENCRYPTED TEXT: {cipher_text}")

# 3. Decryption
prep_dec = prepare_text(cipher_text, False)
plain_text = process_logic(prep_dec, matrix, False)
print(f"\nFINAL DECRYPTED TEXT: {plain_text}")
