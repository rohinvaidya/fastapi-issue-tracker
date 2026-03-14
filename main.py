from fastapi import FastAPI

from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware

from app.routes.issues import router as issues_router
from app.routes.auth import router as auth_router

app = FastAPI(
    title="Issue Tracker API",
    description="A simple API for tracking issues, built with FastAPI.",
    version="1.0.0"
)

app.middleware("http")(timing_middleware)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"])

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(auth_router)
app.include_router(issues_router)