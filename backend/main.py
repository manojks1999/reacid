import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from app.api.routes import router as api_router
from app.core.config import settings

app = FastAPI(title="ReacidAPI")

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to Reacid API"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.BACKEND_SERVER_HOST,
        port=settings.BACKEND_SERVER_PORT,
        reload=True,
        workers=settings.BACKEND_SERVER_WORKERS
    )