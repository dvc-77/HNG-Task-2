# HNG-Stage-Two

## Built with

- FastAPI
- PostgreSQL
- Render

### Testing
- Thunderbird Client

### Features:

- Retrieve Slack name and track information.
- Get the current day of the week and UTC time.
- Access GitHub URLs for the executed file and the project's source code.
- Response format adheres to JSON standards.
- Endpoint accessible publicly on Render.

## Endpoints

- `/api`: 
   - Method: POST
   - Body:
        ```json
        {
          "name": "Neil Ohene"
        }
        ```
### Response
```json
{
  "name": "Neil Ohene",
  "date_created": "2023-09-15T19:53:53Z",
  "last_updated": "2023-09-15T19:53:53Z",
  "message": "Person Created Successfuly"
}
```

- `/api`: 
   - Method: GET
   - Purpose: Return all users
   - Example: GET https://hng-stageone-task.onrender.com/api

 ### Response
```json
{
   {
    "id": 1,
    "name": "neil ohene"
  },
  {
    "id": 2,
    "name": "albert essilfie"
  },
  {
    "id": 3,
    "name": "kwesi brako"
  }
}
```

- `/api/{id}`: 
   - Method: GET
   - Purpose: Return specific user
   - Example: GET https://hng-stageone-task.onrender.com/api/1

 ### Response
```json
{

    "id": 1,
    "name": "neil ohene"
}
```

- `/api/{id}`: 
   - Method: PATCH
   - Purpose: Update specific user
   - Example: PUT https://hng-stageone-task.onrender.com/api/1

- Body:
        ```json
        {
          "name": "Nsiah otoo"
        }
        ```

 ### Response
```json
{
  "name": "nsiah otoo",
  "last_updated": "2023-09-15T19:53:53Z",
  "message": "Name updated to Nsiah Otoo successfully"
}
```

- `/api/{id}`:
    - Method: DELETE
    - Purpose: Delete specific user
    - Example: DELETE https://hng-stageone-task.onrender.com/api/1
    
     ### Response
    ```json
    {
      "message": "Person deleted successfully"
    }
    ```

### Getting Started:
Follow these steps to run this repo locally:

- Fork or Clone the repository: git clone https://github.com/dvc-77/HNG-Task-2.git
- Create a virtual environment and install dependencies using `pip install -r requirements.txt`.
- Run the FastAPI app using `uvicorn main:app --reload --port=8000`.
- Access the API at http://localhost:8000/api and provide the required psyload. 
    - Example: `/api?slack_name=Neil%20Ohene&track=backend`