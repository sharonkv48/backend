from pydantic import BaseModel

class responseStudent(BaseModel):
    id: str
    user_id: int
    name: str
    username: str
    email: str
    age: int
    track: str
    