from fastapi import FastAPI
from config.routes import routing
from config.database import engine
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import SQLAlchemyError
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True,docs_url="/api/documentations")
app.add_middleware(CORSMiddleware,  
                        allow_origins=["/"], 
                        allow_credentials=True,
                        allow_methods=["*"],
                        allow_headers=["*"]
                        )
def main():
    app.mount("/assets",StaticFiles(directory="public"),name="assets",)
    try:
        engine.connect()
    except SQLAlchemyError as error:
        raise error
    routing(app)

    


@app.on_event("startup")
def startUp():
    main()