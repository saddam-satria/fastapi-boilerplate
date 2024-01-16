


def successResponse(message: str, statusCode: int, data):
    return {
        "message" : message,
        "statusCode": statusCode,
        "data": data
    }
def errorResponse(message: str, statusCode: int, data = None):
    return {
        "message" : message,
        "statusCode": statusCode,
        "data": data
    }