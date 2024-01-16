from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR,".env"))

DB_URL=os.environ["DATABASE_URL"]
SECRET_KEY=os.environ["SECRET_KEY"]