import re


def assess(password):
    checks = {
        "length": len(password) >= 12,
        "lowercase": bool(re.search(r"[a-z]", password)),
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "symbol": bool(re.search(r"[^A-Za-z0-9]", password)),
        "no_common_sequence": not any(part in password.lower() for part in ("1234", "password", "qwerty", "abcd")),
    }
    score = sum(checks.values())
    label = "strong" if score >= 5 else "moderate" if score >= 3 else "weak"
    return {"score": score, "rating": label, "checks": checks}


if __name__ == "__main__":
    value = input("Enter a password to evaluate: ")
    print(assess(value))
