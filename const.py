import os
from dotenv import load_dotenv

# Load your environment variables from .env file (Cloudflare API Token)
load_dotenv()


API_KEY = os.environ.get("CF_API_KEY")
ZONE_ID = os.environ.get("ZONE_ID")