def validate_username(username):
    if len(username) < 5 or len(username) > 20:
        return False
    for character in username:
        if not character.isalnum():
            return False
    return True


def validate_password(password):
    if len(password) < 8 or len(password) > 20:
        return False
    for character in password:
        if not character.isalnum():
            return False
    return True
