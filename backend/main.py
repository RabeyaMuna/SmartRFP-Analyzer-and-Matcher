from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from api.authentication.login_api import router as login_router
from api.authentication.signup import router as signup_router
from api.authentication.user_api import router as users_router
from api.file_upload.file_upload_azure_blob import router as single_file_upload_azure_blob

load_dotenv()

app = FastAPI()

# Include the router containing your API endpoints
app.include_router(login_router)
app.include_router(signup_router)
app.include_router(users_router)
app.include_router(single_file_upload_azure_blob)

# Configure CORS middleware
origins = [
    "http://localhost:3000",
    "http://172.206.235.109:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
    expose_headers=['*']
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
