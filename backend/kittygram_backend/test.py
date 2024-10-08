import os 

from dotenv import load_dotenv
load_dotenv()

print(type(os.getenv('DEBUG')))
print(os.getenv('DEBUG'))