# app/auth/auth_router.py
from fastapi import APIRouter, Depends
from config import supabase,settings
from functools import wraps
from fastapi import Request, HTTPException

AUTHROUTER = APIRouter()

def protected(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Authorization header missing")

        # Decode the token and attach user info to request object
        user = supabase.auth.get_user(token)
        if not user:
            raise HTTPException(status_code=401, detail="Unauthorized")

        request.state.user = user.user.model_dump()
        return await func(request, *args, **kwargs)
    return wrapper


@AUTHROUTER.post("/register")
async def register_user(email: str, password: str):
    # Register user with Supabase
    response = supabase.auth.sign_up({
                "email": email,
                "password": password,
                })
    return response

@AUTHROUTER.post("/login")
async def login(email: str, password: str):
    # Sign in user with Supabase
    response = supabase.auth.sign_in_with_password({"email": email, "password": password})
    return response

