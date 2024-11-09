from pydantic import BaseModel

class responseMentor(BaseModel):
    id: str
    user_id: int
    name: str
    username: str
    email: str
    track: str  
