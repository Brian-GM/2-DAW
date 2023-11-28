def is_username(username: str) -> bool:
    username = username.strip()
    if " " in username:
        return False


def is_password(password: str) -> bool:
    password: str = password
    if len(password) > 8:
        if password.isalnum() or password.isalpha():
            return False
        else:
            return True
    else:
        return False
