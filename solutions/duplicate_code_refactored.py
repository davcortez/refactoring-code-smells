def validate_input(input_string, min_length, max_length):
    if len(input_string) < min_length or len(input_string) > max_length:
        return False
    for character in input_string:
        if not character.isalnum():
            return False
    return True


def validate_username(username):
    return validate_input(username, 5, 20)


def validate_password(password):
    return validate_input(password, 8, 20)
