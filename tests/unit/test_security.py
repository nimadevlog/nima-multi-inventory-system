from app.core.security import hash_password, verify_password


def test_hash_is_not_plaintext_and_verifies():
    hashed = hash_password("correct horse battery")

    assert hashed != "correct horse battery"
    assert verify_password("correct horse battery", hashed)
    assert not verify_password("wrong password", hashed)
