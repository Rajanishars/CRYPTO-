def caesar_cipher(text, shift, mode):
    result = ""
    # If mode is 'dec', we reverse the shift
    actual_shift = (26 - (shift % 26)) if mode == 'dec' else shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + actual_shift) % 26 + start)
        else:
            result += char
    return result

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def hill_cipher(text, key, mode):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"

    # Extract matrix values [row1_col1, row1_col2, row2_col1, row2_col2]
    a, b, c, d = key[0][0], key[0][1], key[1][0], key[1][1]

    if mode == 'dec':
        det = (a * d - b * c) % 26
        inv_det = mod_inverse(det, 26)
        if inv_det is None:
            return "Error: Matrix not invertible (No Decryption possible)"
        # Swap a & d, negate b & c, multiply by inv_det
        a, b, c, d = (d * inv_det) % 26, (-b * inv_det) % 26, (-c * inv_det) % 26, (a * inv_det) % 26

    res = ""
    for i in range(0, len(text), 2):
        p1, p2 = ord(text[i]) - 65, ord(text[i+1]) - 65
        res += chr(((a * p1 + b * p2) % 26) + 65)
        res += chr(((c * p1 + d * p2) % 26) + 65)
    return res

while True:
    print("\n--- CIPHER MENU ---")
    print("1. Caesar Cipher")
    print("2. Hill Cipher (2x2)")
    print("3. Exit")
    choice = input("Select Cipher (1-3): ")

    if choice == '3':
        break

    msg = input("Enter Text: ")

    if choice == '1':
        s = int(input("Enter Shift Key: "))
        encrypted = caesar_cipher(msg, s, 'enc')
        decrypted = caesar_cipher(encrypted, s, 'dec')

        print("\n--- RESULTS ---")
        print("Original Text: ", msg)
        print("Encrypted Text:", encrypted)
        print("Decrypted Text:", decrypted)

    elif choice == '2':
        print("Enter 2x2 Matrix values:")
        k11 = int(input("Row 1, Col 1: "))
        k12 = int(input("Row 1, Col 2: "))
        k21 = int(input("Row 2, Col 1: "))
        k22 = int(input("Row 2, Col 2: "))
        matrix = [[k11, k12], [k21, k22]]

        encrypted = hill_cipher(msg, matrix, 'enc')
        decrypted = hill_cipher(encrypted, matrix, 'dec')

        print("\n--- RESULTS ---")
        print("Original Text: ", msg.upper().replace(" ", ""))
        print("Encrypted Text:", encrypted)
        print("Decrypted Text:", decrypted)
