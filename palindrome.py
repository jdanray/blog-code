def palindrome(e):
    q = list(e)
    s = list(e)
    while q and s:
        if q.pop(0) is not s.pop():
            return False
    return True
