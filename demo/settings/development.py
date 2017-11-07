from .base import *
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

print("estoy en development")
DEBUG = os.environ.get('DEBUG_DEV')
