from .base import *
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

print("estoy en produccion")

DEBUG = os.environ.get('DEBUG')

ALLOWED_HOST = ['*']

