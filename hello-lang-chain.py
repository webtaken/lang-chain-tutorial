import os
from dotenv import load_dotenv

load_dotenv(".env.development")

API_KEY = os.getenv("OPENAI_API_KEY")

print(API_KEY)