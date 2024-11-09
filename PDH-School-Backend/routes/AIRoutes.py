
from fastapi import APIRouter, Depends
from services.AIservice import generate_response
from services.oAuth2 import get_current_user
from datetime import datetime
from bson import ObjectId
from typing import Optional

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)

@router.get("/ask")
def ask(
    question: str, 
    to_username: Optional[str] = None,  # Make recipient optional
    user: dict = Depends(get_current_user)
):
    # Extract the necessary fields from the authenticated user
    name = user.get("name")
    username = user.get("username")
   
    # Get response
    response = generate_response(
        question=question,
        from_username=username,
        from_name=name,
        to_username=to_username
    )
    
    return {
        "id": str(ObjectId()),
        "from_name": name,
        "from_username": username,
        "to_username": to_username,
        "query": question,
        "response": response,
        "timestamp": datetime.now().isoformat()
    }
