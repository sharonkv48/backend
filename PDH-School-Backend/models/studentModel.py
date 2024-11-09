# from pydantic import BaseModel

# class Student(BaseModel):
#     user_id: int
#     name: str
#     username: str
#     password: str
#     email: str
#     age: int
#     track: str






# from pydantic import BaseModel, EmailStr
# from typing import Optional
# from config.mongoDB import collection
# from fastapi import HTTPException, status

# class Student(BaseModel):
#     user_id: int
#     name: str
#     username: str
#     password: str
#     email: EmailStr
#     age: int
#     track: str

#     @classmethod
#     async def create(cls, data: dict):
#         # Check if username already exists
#         if await collection.find_one({"username": data["username"]}):
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Username already registered"
#             )

#         # Check if email already exists
#         if await collection.find_one({"email": data["email"]}):
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="Email already registered"
#             )

#         # Check if user_id already exists
#         if await collection.find_one({"user_id": data["user_id"]}):
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST,
#                 detail="User ID already registered"
#             )

#         result = await collection.insert_one(data)
#         return cls(**data, id=str(result.inserted_id))


# studentmodel.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from config.mongoDB import collection, mentor_collection  # Import both collections
from fastapi import HTTPException, status

class Student(BaseModel):
    user_id: int
    name: str
    username: str
    password: str
    email: EmailStr
    age: int
    track: str

    @classmethod
    async def create(cls, data: dict):
        # Check if username already exists
        if await collection.count_documents({"username": data["username"]}) > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )

        # Check if email already exists
        if await collection.count_documents({"email": data["email"]}) > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        # Check if user_id already exists in both collection and mentor_collection
        if await collection.count_documents({"user_id": data["user_id"]}) > 0 or \
           await mentor_collection.count_documents({"user_id": data["user_id"]}) > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User ID already registered"
            )

        result = await collection.insert_one(data)
        return cls(**data, id=str(result.inserted_id))
