# import pydantic
#
#
# class Config(pydantic.BaseSettings):
#
#     env_file = '.env'
#     env_file_encoding = 'utf-8'
#     TOKEN: str = None
#
#
# config = Config()



import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    TOKEN: str = os.getenv('TOKEN')

config = Config()