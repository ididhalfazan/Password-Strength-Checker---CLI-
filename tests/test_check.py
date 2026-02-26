from app.checker import evaluate_password


def test_strong_password():
    result = evaluate_password("StrongPass123!")
    assert result["strength"] == "Strong"


def test_weak_password():
    result = evaluate_password("abc")
    assert result["strength"] == "Weak"
