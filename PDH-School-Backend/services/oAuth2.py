
# services/oauth2.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from services.security import verify_token
from config.mongoDB import collection, mentor_collection
from schemas.StudentEntity import studentEntity
from schemas.MentorEntity import mentiorEntity

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token_data = verify_token(token, credentials_exception)
    
    # Check role from token
    if token_data.role == "mentor":
        user = mentor_collection.find_one(
            {"username": token_data.username},
            {'password': 0}
        )
        if user:
            return mentiorEntity(user)
    else:
        user = collection.find_one(
            {"username": token_data.username},
            {'password': 0}
        )
        if user:
            return studentEntity(user)
    
    raise credentials_exception
