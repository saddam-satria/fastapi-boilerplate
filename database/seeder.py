from sqlalchemy.orm import Session
from models import UserCredential
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import bcrypt

def seeder():
    load_dotenv()
    engine = create_engine(os.environ["DATABASE_URL"])
    session = Session(bind=engine)
    password = bcrypt.hashpw("admin".encode("utf-8"), bcrypt.gensalt()).decode()
    user= UserCredential("test@gmail.com",password=password )
    session.add(user)

    session.commit()

if __name__=="__main__":
    seeder()