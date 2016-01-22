def hidden(password, message):
    if not password:
        return True
    elif not message:
        return False
    elif message[0] == password[0]:
        return hidden(password[1:], message[1:])
    elif message[0] in password:					# remember: this is a linear-time operation
        return False	
    else: 
        return hidden(password, message[1:])

password = "ABC"
message = "HAPPYBIRTHDAYCACEY"
message = "TRAGICBIRTHDAYCACEY"
message = "HAPPYBIRTHDAY"
message = "SOMECHORESARETOUGH"
password = "SECRET"
message = "SOMECHEERSARETOUGH"

print hidden(password, message)
