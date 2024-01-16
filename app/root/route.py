from fastapi import APIRouter


rootRoute = APIRouter()


@rootRoute.get("/")
def rootGet():
    return {
        "message":"welcome to fastapi boilerplate"
    }


