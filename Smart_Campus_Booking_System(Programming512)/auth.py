import hashlib

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def verify_password(password, stored_hash):

    return (
        hashlib.sha256(
            password.encode()
        ).hexdigest()
        ==
        stored_hash
    )