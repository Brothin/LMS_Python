from bson import ObjectId
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB Atlas connection string
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)

# Get the database
db = client["Cluster0"]

# Get the collection
collection = db["students"]

# Create FastAPI app
app = FastAPI()

# Define data model
class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

# CRUD operations
@app.post("/students", status_code=201)
async def create_students(student: Student):
    student_dict = student.dict()
    inserted = collection.insert_one(student_dict)
    return {"id": str(inserted.inserted_id)}

@app.get("/students", status_code=200)
async def list_students(country: str = None, age: int = None):
    filter_dict = {}
    if country:
        filter_dict["address.country"] = country
    if age:
        filter_dict["age"] = {"$gte": age}

    students = collection.find(filter_dict)
    response_data = {"data": []}
    for student in students:
        response_data["data"].append({"name": student["name"], "age": student["age"]})
    return response_data

@app.get("/students/{student_id}", status_code=200)
async def fetch_student(student_id: str):
    student = collection.find_one({"_id": ObjectId(student_id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student["id"] = str(student["_id"])
    del student["_id"]
    del student["id"]
    return student

@app.patch("/students/{student_id}", status_code=204)
async def update_student(student_id: str, student_update: Student):
    updated_count = collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student_update.dict()},
    )
    if updated_count.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}

@app.delete("/students/{student_id}", status_code=200)
async def delete_student(student_id: str):
    deleted_count = collection.delete_one({"_id": ObjectId(student_id)})
    if deleted_count.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}
