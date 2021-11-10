def pluralize(total, singular, plural=None):
    assert isinstance(total, int) and total >= 0, "total must be positive"
    if not plural:
        plural = singular + 's'
        string = singular if total <= 1 else plural
        return f"{total} {string}"
