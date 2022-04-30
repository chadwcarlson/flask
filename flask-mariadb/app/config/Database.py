import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

class DbConfig:
    def __init__(self):
        self.DB_USERNAME = os.getenv("DB_NAME_MYSQL")
        self.DB_PASSWORD = ""
        self.DB_HOST = os.getenv("DB_HOST_MYSQL")
        self.DB_PORT = os.getenv("DB_PORT_MYSQL")
        self.DB_NAME = os.getenv("DB_NAME_MYSQL")

    def getUri(self):
        return "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(self.DB_USERNAME, self.DB_PASSWORD, self.DB_HOST,
                                                              self.DB_PORT, self.DB_NAME)
