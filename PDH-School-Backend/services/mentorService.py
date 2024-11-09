
from fastapi import HTTPException
from models.mentorModel import Mentor
from config.mongoDB import mentor_collection
from schemas.MentorEntity import mentiorEntity, mentorsEntity
from services.security import Hash

def genrate_mentor(mentor: Mentor):
    # Check if username already exists in either collection
    if mentor_collection.find_one({"username": mentor.username}):
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    
    # Check if email already exists
    if mentor_collection.find_one({"email": mentor.email}):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    # Create mentor dictionary and hash password
    mentor_dict = mentor.model_dump()
    mentor_dict["password"] = Hash.hash_password(mentor_dict["password"])
    
    # Insert into database
    result = mentor_collection.insert_one(mentor_dict)
    mentor_dict['id'] = str(result.inserted_id)
    
    # Remove password from response
    response_dict = {k: v for k, v in mentor_dict.items() if k != 'password'}
    return mentiorEntity(response_dict)

def get_all_mentor():
    mentors = mentor_collection.find({}, {'password': 0})  # Exclude password
    return mentorsEntity(mentors)

def get_mentor_by_username(username: str):
    mentor = mentor_collection.find_one({"username": username}, {'password': 0})
    if not mentor:
        raise HTTPException(status_code=404, detail="Mentor not found")
    return mentiorEntity(mentor)

def update_mentor(username: str, mentor: Mentor):
    # Check if mentor exists
    existing_mentor = mentor_collection.find_one({"username": username})
    if not existing_mentor:
        raise HTTPException(status_code=404, detail="Mentor not found")
    
    # Check if new username is taken
    if username != mentor.username and mentor_collection.find_one({"username": mentor.username}):
        raise HTTPException(status_code=400, detail="Username already taken")
    
    # Check if new email is taken
    if existing_mentor["email"] != mentor.email and mentor_collection.find_one({"email": mentor.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Update mentor
    mentor_dict = mentor.model_dump()
    mentor_dict["password"] = Hash.hash_password(mentor_dict["password"])
    
    mentor_collection.update_one(
        {"username": username},
        {"$set": mentor_dict}
    )
    
    # Return updated mentor without password
    updated_mentor = mentor_collection.find_one({"username": mentor.username}, {'password': 0})
    return mentiorEntity(updated_mentor)

def delete_mentor(username: str):
    result = mentor_collection.delete_one({"username": username})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Mentor not found")
    return None
