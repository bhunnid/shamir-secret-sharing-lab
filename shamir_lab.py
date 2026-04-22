import random

# -------------------------------
# Modular inverse
# -------------------------------
def mod_inverse(a, p):
    return pow(a, -1, p)
# -------------------------------
# Generate Shares
# -------------------------------
def generate_shares(secret, t, n, p):
    # Random polynomial coefficients
    coeffs = [secret] + [random.randint(1, p-1) for _ in range(t-1)]

    def polynomial(x):
        return sum(coeffs[i] * (x ** i) for i in range(len(coeffs))) % p

    shares = [(x, polynomial(x)) for x in range(1, n+1)]
    return shares
# -------------------------------
# Reconstruct Secret
# -------------------------------
def reconstruct_secret(shares, p):
    secret = 0

    for j, (xj, yj) in enumerate(shares):
        numerator = 1
        denominator = 1

        for m, (xm, _) in enumerate(shares):
            if m != j:
                numerator = (numerator * (-xm)) % p
                denominator = (denominator * (xj - xm)) % p

        lagrange_coeff = numerator * mod_inverse(denominator, p)
        secret = (secret + yj * lagrange_coeff) % p

    return secret
# -------------------------------
# Additive Sharing
# -------------------------------
def additive_sharing(secret, n, p):
    shares = [random.randint(0, p-1) for _ in range(n-1)]
    last_share = (secret - sum(shares)) % p
    shares.append(last_share)
    return shares
def reconstruct_additive(shares, p):
    return sum(shares) % p
# -------------------------------
# MAIN TEST
# -------------------------------
if __name__ == "__main__":
    p = 2089
    secret = 1234
    t = 3
    n = 5
    print("=== Shamir Secret Sharing ===")
    shares = generate_shares(secret, t, n, p)
    print("Shares:", shares)
    subset = shares[:3]
    recovered = reconstruct_secret(subset, p)
    print("Recovered Secret (3 shares):", recovered)
    # Try with fewer shares
    subset_fail = shares[:2]
    recovered_fail = reconstruct_secret(subset_fail, p)
    print("Recovered Secret (2 shares):", recovered_fail)
    print("\n=== Additive Secret Sharing ===")
    add_shares = additive_sharing(secret, n, p)
    print("Additive Shares:", add_shares)
    recovered_add = reconstruct_additive(add_shares, p)
    print("Recovered Additive Secret:", recovered_add)