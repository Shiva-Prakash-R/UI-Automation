from fastapi import FastAPI

app = FastAPI(title="API For testing")

#get API - Home page
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

# GET API - Get user details
@app.get("/user")
def get_user():
    return {
        "id": 1,
        "name": "Shiva",
        "role": "Python Developer"
    }

# Get API - Get user details by ID
@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    return {
        "id": user_id,
        "name": "Shiva",
        "role": "Python Developer",
        "Message": "User details fetched successfully"
    }