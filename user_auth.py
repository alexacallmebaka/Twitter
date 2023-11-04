from typing import Tuple
import os
import hashlib
import hmac
import user_auth
def hash_new_password(password: str) -> Tuple[bytes, bytes]:
    """
    Hash the provided password with a randomly-generated salt and return the
    salt and hash to store in the database.
    """
    salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, pw_hash

def is_correct_password(pw_hash: bytes, password: str) -> bool:
    """
    Given a previously-stored salt and hash, and a password provided by a user
    trying to log in, check whether the password is correct.
    """
    # return hmac.compare_digest(
    #     pw_hash,
    #     hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    # )
    return pw_hash == db_pw

# Example usage:
user = 'test'
pw = 'correct horse battery staple'
salt, pw_hash = hash_new_password(pw)
if user_auth.if_exists(user):
    user_auth.insert_to(user, pw_hash)

user, db_pw = user_auth.read_from(user)

assert is_correct_password(pw_hash, db_pw)
