from re import match


def ip_verification(ip: str):
    regex = r"^(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})){3}$"
    matched = match(regex, ip)
    if matched is None:
        return False
    elif matched is not None:
        return True
