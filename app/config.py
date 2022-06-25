import pydantic


class Config(pydantic.BaseSettings):
    TOKEN: str


config = Config()
