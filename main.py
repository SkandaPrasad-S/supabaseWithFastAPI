# app/main.py
from fastapi import FastAPI,Request
from routers.auth.auth_api import AUTHROUTER, protected

app = FastAPI()

# Include the authentication router
app.include_router(AUTHROUTER, prefix="/auth")

@app.get("/protected-route")
@protected
async def protected_route(request: Request):
    user = request.state.user
    print(user["email"])
    return {"message": f'{user["email"]} This is a protected route.'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="localhost", port="8080")
