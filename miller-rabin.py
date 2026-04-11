def power(base, exp, mod):
    res = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def miller_rabin(n):
    if n <= 1 or n == 4: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    # Using fixed bases 2 and 3 instead of 'import random'
    bases = [2, 3]
    for a in bases:
        if a >= n: break
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            continue

        composite = True
        temp_d = d
        while temp_d != n - 1:
            x = (x * x) % n
            temp_d *= 2
            if x == n - 1:
                composite = False
                break
            if x == 1: return False
        if composite: return False
    return True

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

while True:
    print("\n--- MATHEMATICAL MENU ---")
    print("1. Miller-Rabin Primality Test")
    print("2. GCD (Greatest Common Divisor)")
    print("3. Extended Euclidean Algorithm")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == '1':
        num = int(input("Enter number: "))
        if miller_rabin(num):
            print(f"Result: {num} is PRIME")
        else:
            print(f"Result: {num} is COMPOSITE")

    elif choice == '2':
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        print(f"GCD: {get_gcd(n1, n2)}")

    elif choice == '3':
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        gcd, x, y = extended_gcd(a, b)
        print(f"GCD: {gcd}, x: {x}, y: {y}")
        print(f"Equation: ({a} * {x}) + ({b} * {y}) = {gcd}")

    elif choice == '4':
        break
