# Library Management System - Backend API

This project implements the backend API layer for a Library Management System. It utilizes FastAPI for building the API endpoints and leverages MongoDB Atlas for database storage. It provides endpoints for CRUD (Create, Read, Update, Delete) operations on student records.

## Tech Stack
• Language: Python

• Framework: FastAPI

• Database: MongoDB (MongoDB Atlas)

## Deployed Link
https://lms-python.onrender.com/

## Dependencies
• PyMongo/Motor (for MongoDB interaction)

• Pydantic (for data validation and modeling)

• dotenv (for environment variable management)

## Setup
1. Clone the repository:
```
git clone https://github.com/Brothin/LMS_Python
cd LMS_Python
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Set up MongoDB Atlas:
   
• Create a free account on MongoDB Atlas.

• Create an M0 Free Tier cluster.

• Obtain the connection URI.

4. Create a `.env` file in the root directory and add the MongoDB URI:
```
MONGO_URI=<your-mongodb-uri>
```
5. Run the FastAPI application:
```
uvicorn main:app --reload
```

## Endpoints
### Create Student:

• Method: POST

• URL: /students/

• Body: JSON object representing a Student (see data model)

• Response: JSON object with the newly created student's ID

### Get Students:

• Method: GET

• URL: /students/

• Query parameters:

▸ country: Filter students by country (optional)

▸ age: Filter students by age (greater than or equal to) (optional)

• Response: JSON object with a list of student details (name and age)

### Get Student:

• Method: GET

• URL: /students/{student_id}

• Path parameter: student_id

• Response: JSON object with the details of the requested student

### Update Student:

• Method: PATCH

• URL: /students/{student_id}

• Path parameter: student_id

• Body: JSON object representing the updated student data (partial update)

• Response: Empty response on successful update (status code 204)

### Delete Student:

• Method: DELETE

• URL: /students/{student_id}

• Path parameter: student_id

• Response: Empty response on successful deletion (status code 200)

## Data Model
The Student data model is defined using Pydantic and consists of the following fields:

• name: String (required)

• age: Integer (required)

• address: Nested Address model (optional)

▸ city: String (required)

▸ country: String (required)

## Error Handling
`404 Not Found`: If a requested student record is not found.

## Notes
• Ensure that MongoDB Atlas URI is correctly set in the `.env` file.

• The API automatically reloads on code changes when running with `uvicorn --reload`.
