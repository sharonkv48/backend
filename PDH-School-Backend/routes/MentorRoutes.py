from fastapi import APIRouter , status
from typing import List
from models.mentorModel import Mentor
from responseModel.responseMentor import responseMentor
from services.mentorService import genrate_mentor , update_mentor , get_all_mentor , get_mentor_by_username , delete_mentor


router = APIRouter(
    prefix="/mentor",
    tags=["Mentor"],
)


@router.get("/",  status_code=status.HTTP_200_OK ,response_model=List[responseMentor])
def get_all():
    return get_all_mentor()

@router.get("/{username}", status_code=status.HTTP_200_OK, response_model=responseMentor)
def get(username: str):
    return get_mentor_by_username(username)

@router.post("/",  status_code=status.HTTP_201_CREATED,response_model=responseMentor)
def create(mentor: Mentor):
    return genrate_mentor(mentor)

@router.put("/{username}", status_code=status.HTTP_200_OK, response_model=responseMentor)
def update(username: str , mentor: Mentor):
    return update_mentor(username , mentor)

@router.delete("/{username}", status_code=status.HTTP_204_NO_CONTENT)
def delete(username: str):
    return delete_mentor(username)