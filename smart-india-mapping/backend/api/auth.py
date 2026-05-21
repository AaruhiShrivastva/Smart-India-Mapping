from fastapi import APIRouter, HTTPException, status
from datetime import timedelta
from backend.models import User, LoginRequest, TokenResponse, UserResponse
from backend.auth import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from backend.database import user_exists, create_user, get_user_by_username, get_user_by_id
from jose import jwt

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse)
async def register(user: User):
    """Register a new user"""
    if user_exists(user.username, user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists"
        )
    
    if len(user.password) < 6:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 6 characters"
        )
    
    created_user = create_user(user.username, user.email, user.password)
    return UserResponse(
        id=created_user["id"],
        username=created_user["username"],
        email=created_user["email"]
    )

@router.post("/login", response_model=TokenResponse)
async def login(credentials: LoginRequest):
    """Login user and return JWT token"""
    user = get_user_by_username(credentials.username)
    
    if not user or not verify_password(credentials.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=UserResponse(
            id=user["id"],
            username=user["username"],
            email=user["email"]
        )
    )

@router.get("/me", response_model=UserResponse)
async def get_current_user(token: str):
    """Get current user info"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        user = get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        return UserResponse(
            id=user["id"],
            username=user["username"],
            email=user["email"]
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")
