import re


def has_uppercase(password: str) -> bool:
    """Return True if the password contains at least one uppercase letter."""
    return any(char.isupper() for char in password)


def has_lowercase(password: str) -> bool:
    """Return True if the password contains at least one lowercase letter."""
    return any(char.islower() for char in password)


def has_number(password: str) -> bool:
    """Return True if the password contains at least one numeric digit."""
    return any(char.isdigit() for char in password)


def has_special(password: str) -> bool:
    """Return True if the password contains at least one special character."""
    return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))


def is_long_enough(password: str, min_length: int) -> bool:
    """
    Return True if the password meets the minimum length requirement.

    Args:
        password (str): Password to check.
        min_length (int): Minimum required length.
    """
    return len(password) >= min_length


def evaluate_password(password: str, min_length: int = 8) -> dict:
    """
    Evaluate password strength based on length and character diversity.

    Scoring Criteria:
        - Minimum length
        - Uppercase letter
        - Lowercase letter
        - Number
        - Special character

    Returns:
        dict: {
            "score": int (0–5),
            "strength": str ("Weak", "Medium", "Strong"),
            "suggestions": list[str]
        }
    """
    score = 0
    suggestions = []

    if is_long_enough(password, min_length):
        score += 1
    else:
        suggestions.append(
            f"Password should be at least {min_length} characters long."
        )

    if has_uppercase(password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if has_lowercase(password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if has_number(password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    if has_special(password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Strength classification
    if score <= 2:
        strength = "Weak"
    elif score in (3, 4):
        strength = "Medium"
    else:
        strength = "Strong"

    return {
        "score": score,
        "strength": strength,
        "suggestions": suggestions
    }