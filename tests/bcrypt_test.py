import bcrypt


def hashText(plainText:str) -> str:
    return bcrypt.hashpw(plainText.encode("utf-8"), bcrypt.gensalt()).decode()

def verifyHashedText(plainText:str, hashedText: str) -> bool:
    plainByte = plainText.encode()
    return bcrypt.checkpw(plainByte, hashedText.encode())

    
class TestBcrypt:
    def test_success(self):
        password = "test"
        hashedPassword = hashText(password)

        result = verifyHashedText(password,hashedPassword)

        assert result == True
 