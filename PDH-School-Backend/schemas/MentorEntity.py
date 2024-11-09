

# def mentiorEntity(item) -> dict:
#     return {
#         "id": str(item.get("_id", "")),
#         "user_id": item.get("user_id", 0),
#         "name": item.get("name", ""),
#         "username": item.get("username", ""),
#         "email": item.get("email", ""),
#         "password": item.get("password", ""),
#         "track": item.get("track", ""),
#     }

# def mentorsEntity(items) -> list:
#     return [mentiorEntity(item) for item in items]



# schemas/MentorEntity.py
def mentiorEntity(item) -> dict:
    return {
        "id": str(item.get("_id", "")),
        "user_id": item.get("user_id", 0),
        "name": item.get("name", ""),
        "username": item.get("username", ""),
        "email": item.get("email", ""),
        "track": item.get("track", "")
    }

def mentorsEntity(items) -> list:
    return [mentiorEntity(item) for item in items]