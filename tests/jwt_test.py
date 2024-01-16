import jwt


def generateTokenJwt(payload) -> str:
    return jwt.encode(payload=payload, key="SECRET_KEY")

def verifyTokenJWt(token:str):
    try:
        return jwt.decode(token,"SECRET_KEY", algorithms=["HS256"])
    except jwt.ExpiredSignatureError as e:
        raise e
    except jwt.InvalidTokenError as e:
        raise e


class TestJWT:
    def test_success(self):
        payload= {
            "id":1,
            "name": "test"
        }


        jwt= generateTokenJwt(payload=payload)

        result = verifyTokenJWt(jwt)

        assert result == payload
   