from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost",          # Specific origin (e.g., for local development)
    "http://localhost:3000",     # Allow requests from your frontend (React or Angular, etc.)
    "*",                         # Allow requests from any origin (can be restricted if needed)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Origins allowed
    allow_credentials=True,          # Allow cookies to be sent with the requests
    allow_methods=["*"],             # HTTP methods allowed (GET, POST, PUT, etc.)
    allow_headers=["*"],             # HTTP headers allowed in the request
)

# Hello World route
@app.get("/")
def read_root():
    return {"message": "Hello World"}
