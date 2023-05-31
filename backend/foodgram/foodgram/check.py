import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

db_engine = os.getenv('DB_ENGINE')

print(BASE_DIR)
