# from  pydantic import BaseModel

# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: str | None = None


# class Login(BaseModel):
#     username: str
#     password: str   






# from pydantic import BaseModel

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     username: str | None = None

# class Login(BaseModel):
#     username: str
#     password: str


# models/token.py
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
    role: str | None = None

class Login(BaseModel):
    username: str
    password: str