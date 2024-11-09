
# services/authenticationService.py
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .security import create_access_token, Hash
from schemas.StudentEntity import studentEntity
from schemas.MentorEntity import mentiorEntity
from config.mongoDB import collection, mentor_collection
import logging

logger = logging.getLogger(__name__)

def authenticate_user(form_data: OAuth2PasswordRequestForm):
    # First try student collection
    user = collection.find_one({"username": form_data.username})
    is_mentor = False
    
    # If not found in student collection, try mentor collection
    if not user:
        user = mentor_collection.find_one({"username": form_data.username})
        is_mentor = True
        
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verify password
    if not Hash.verify_password(form_data.password, user['password']):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generate token with role information
    access_token = create_access_token(
        data={
            "sub": user['username'],
            "role": "mentor" if is_mentor else "student"
        }
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

