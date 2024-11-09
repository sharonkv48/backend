from fastapi import FastAPI
from routes.StudentRouter import router as student_router
from routes.AIRoutes import router as ai_router
from routes.MentorRoutes import router as mentor_router
from routes.authenticationRoute import router as auth_router


app = FastAPI()
app.include_router(student_router)
app.include_router(ai_router)
app.include_router(mentor_router)
app.include_router(auth_router)

