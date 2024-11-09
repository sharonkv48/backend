from fastapi import APIRouter , status , Depends, HTTPException
from typing import List
from models.studentModel import Student
from services.oAuth2 import get_current_user
from responseModel.responseStudent import responseStudent
from services.studentService import genrate_student , update_student , get_all_student , get_student_by_username , delete_student

router = APIRouter(
    prefix="/student",
    tags=["Student"],
)

@router.post("/",  status_code=status.HTTP_201_CREATED,response_model=responseStudent)
def create(student: Student):
    return genrate_student(student)


@router.get("/",  status_code=status.HTTP_200_OK ,response_model=List[responseStudent])
def get_student( current_user: Student = Depends(get_current_user)):   
    return get_all_student()


@router.get("/{username}", status_code=status.HTTP_200_OK, response_model=responseStudent)
def get(username: str):
    return get_student_by_username(username)


@router.put("/{username}", status_code=status.HTTP_200_OK, response_model=responseStudent)
def update(username: str , student: Student):
    return update_student(username , student)




@router.delete("/{username}", status_code=status.HTTP_204_NO_CONTENT)
def delete(username: str):
    return delete_student(username)