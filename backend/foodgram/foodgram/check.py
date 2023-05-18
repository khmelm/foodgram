import os
from dotenv import load_dotenv

from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

db_engine = os.getenv('DB_ENGINE')

print(db_engine)
