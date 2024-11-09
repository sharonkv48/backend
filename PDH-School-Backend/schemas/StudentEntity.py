# def studentEntity(item) -> dict:
#     return {
#         "id": str(item.get("_id", "")),
#         "user_id": item.get("user_id", 0),
#         "name": item.get("name", ""),
#         "username": item.get("username", ""),
#         "email": item.get("email", ""),
#         "age": item.get("age", 0),
#         "track": item.get("track", ""),
#     }

# def studentsEntity(items) -> list:
#     return [studentEntity(item) for item in items]



# schemas/StudentEntity.py
def studentEntity(item) -> dict:
    return {
        "id": str(item.get("_id", "")),
        "user_id": item.get("user_id", 0),
        "name": item.get("name", ""),
        "username": item.get("username", ""),
        "email": item.get("email", ""),
        "age": item.get("age", 0),
        "track": item.get("track", ""),
    }

def studentsEntity(items) -> list:
    return [studentEntity(item) for item in items]


