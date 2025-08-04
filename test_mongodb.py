from urllib.parse import quote_plus
from pymongo import MongoClient
from pymongo.server_api import ServerApi  # ✅ FIXED

# Raw credentials
username = "dhakadarjun678"
password = "arjun@123"  # Replace with your actual password

# URL-encode username and password
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# MongoDB URI
uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.j5ds4e7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create MongoClient
client = MongoClient(uri, server_api=ServerApi('1'))

# Test the connection
try:
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection failed:", e)