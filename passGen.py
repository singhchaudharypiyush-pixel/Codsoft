
import string, secrets

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    pools = []
    if use_lower:   pools.append(string.ascii_lowercase)
    if use_upper:   pools.append(string.ascii_uppercase)
    if use_digits:  pools.append(string.digits)
    if use_symbols: pools.append("!@#$%^&*()-_=+[]{};:,.?/")

    if not pools:
        raise ValueError("Select at least one character set.")
    if length < len(pools):
        raise ValueError(f"Length must be at least {len(pools)} to include all selected types.")

    # Guarantee at least one char from each chosen set
    password_chars = [secrets.choice(p) for p in pools]
    all_chars = "".join(pools)
    password_chars += [secrets.choice(all_chars) for _ in range(length - len(password_chars))]
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)

def yes_no(prompt):
    return input(prompt + " (y/n): ").strip().lower().startswith("y")

def main():
    print("=== PASSWORD GENERATOR ===")
    try:
        length = int(input("Desired length (e.g., 12): ").strip() or "12")
    except ValueError:
        length = 12
    use_lower  = yes_no("Include lowercase?")
    use_upper  = yes_no("Include uppercase?")
    use_digits = yes_no("Include digits?")
    use_symbols= yes_no("Include symbols?")
    try:
        pw = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
        print("\nGenerated Password:", pw)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
