# from models.studentModel import Student
# from responseModel.responseStudent import responseStudent
# from fastapi import HTTPException
# from config.mongoDB import collection
# from schemas.StudentEntity import studentEntity , studentsEntity



# def genrate_student(student: Student):
#     student_dict = student.model_dump()
#     result = collection.insert_one(student_dict)
#     student_dict['id'] = str(result.inserted_id)
#     return studentEntity(student_dict)


# def get_student_by_username(username: str):
#     student = collection.find_one({"username": username})
#     if student is None:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return studentEntity(student)

# def get_all_student():
#     student = collection.find()
#     return studentsEntity(student)


# def update_student(username: str , student: Student):
    
#     collection.update_one({"username": username}, {"$set": student.model_dump()})
#     existing_student = collection.find_one({"username": username})

#     if existing_student is None:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return studentEntity(existing_student)
        
# def delete_student(username: str):
#     collection.delete_one({"username": username})
#     return None


# services/studentService.py
from models.studentModel import Student
from responseModel.responseStudent import responseStudent
from fastapi import HTTPException
from config.mongoDB import collection
from schemas.StudentEntity import studentEntity, studentsEntity
from services.security import Hash

def genrate_student(student: Student):
    # Validate if username already exists
    if collection.find_one({"username": student.username}):
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    
    # Validate if email already exists
    if collection.find_one({"email": student.email}):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    # Create student dictionary and hash password
    student_dict = student.model_dump()
    student_dict["password"] = Hash.hash_password(student_dict["password"])
    
    # Insert into database
    result = collection.insert_one(student_dict)
    student_dict['id'] = str(result.inserted_id)
    
    # Remove password from response
    response_dict = {k: v for k, v in student_dict.items() if k != 'password'}
    return studentEntity(response_dict)

def get_all_student():
    students = collection.find({}, {'password': 0})  # Exclude password field
    return studentsEntity(students)

def get_student_by_username(username: str):
    student = collection.find_one({"username": username}, {'password': 0})  # Exclude password field
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return studentEntity(student)

def update_student(username: str, student: Student):
    # Check if student exists
    existing_student = collection.find_one({"username": username})
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Check if new username is taken (if username is being changed)
    if username != student.username and collection.find_one({"username": student.username}):
        raise HTTPException(status_code=400, detail="Username already taken")
    
    # Check if new email is taken (if email is being changed)
    if existing_student["email"] != student.email and collection.find_one({"email": student.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Update student
    student_dict = student.model_dump()
    student_dict["password"] = Hash.hash_password(student_dict["password"])
    
    collection.update_one(
        {"username": username},
        {"$set": student_dict}
    )
    
    # Return updated student without password
    updated_student = collection.find_one({"username": student.username}, {'password': 0})
    return studentEntity(updated_student)

def delete_student(username: str):
    result = collection.delete_one({"username": username})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return None