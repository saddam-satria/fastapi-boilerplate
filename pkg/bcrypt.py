import bcrypt


def hashText(plainText:str) -> str:
    return bcrypt.hashpw(plainText.encode("utf-8"), bcrypt.gensalt()).decode()

def verifyHashedText(plainText:str, hashedText: str) -> bool:
    plainByte = plainText.encode()
    return bcrypt.checkpw(plainByte, hashedText.encode())

    