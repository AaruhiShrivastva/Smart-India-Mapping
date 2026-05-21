from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .api import geospatial, auth
from .database import user_exists, create_user

# Initialize demo user on startup
def init_demo_user():
    try:
        if not user_exists("testuser", "testuser@smartindia.com"):
            create_user("testuser", "testuser@smartindia.com", "password123")
            print("Demo user created: testuser / password123")
    except Exception as e:
        print(f"Warning: Could not create demo user: {e}")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_demo_user()
    yield
    # Shutdown
    pass

app = FastAPI(title="Smart India Mapping API", version="1.0.0", lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(geospatial.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Smart India Mapping API", "status": "online"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
