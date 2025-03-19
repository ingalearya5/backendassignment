# User Management API

This is a simple User Management API built with FastAPI. It provides endpoints for creating, retrieving, updating, searching, and deleting user records.

## Features

- Create a new user
- Retrieve user details by ID
- Search users by name
- Update user details
- Delete a user

## Installation

1. Clone the repository:

   ```sh
   git clone <your-repository-url>
   cd <your-repository-folder>
   ```

2. Install dependencies:

   ```sh
   pip install fastapi uvicorn pydantic
   ```

3. Run the API:

   ```sh
   uvicorn main:app --reload
   ```

## API Endpoints

### Create a User

**POST** `/users/`

- Request Body:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "phone_no": "1234567890",
    "address": "123 Street, City"
  }
  ```
- Response:
  ```json
  { "message": "User created successfully" }
  ```

### Get User by ID

**GET** `/users/{user_id}`

- Response:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "phone_no": "1234567890",
    "address": "123 Street, City"
  }
  ```

### Search Users

**GET** `/users/search?name=John`

- Response:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "phone_no": "1234567890",
      "address": "123 Street, City"
    }
  ]
  ```

### Update User

**PUT** `/users/{user_id}`

- Request Body:
  ```json
  {
    "name": "John Smith",
    "phone_no": "0987654321",
    "address": "456 Avenue, City"
  }
  ```
- Response:
  ```json
  { "message": "User updated successfully" }
  ```

### Delete User

**DELETE** `/users/{user_id}`

- Response:
  ```json
  { "message": "User deleted successfully" }
  ```

### API Status

**GET** `/`

- Response:
  ```json
  { "message": "User Management API is running" }
  ```

##

