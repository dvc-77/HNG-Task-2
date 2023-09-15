from fastapi import FastAPI, Depends, HTTPException
from fastapi.dependencies.utils import Annotated
import models
from sqlalchemy.orm import Session
import schemas
from database import SessionManager, engine
from datetime import datetime


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionManager()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

#Creating the endpoint to add a new person
@app.post("/api", status_code=201)
async def create_person(person: schemas.PersonBase, db: db_dependency):
    db_person = models.Persons(name=person.name.lower())
    db.add(db_person)
    db.commit()
    current_time_utc = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    response_json = {
                "name": person.name,
                "date_created": current_time_utc,
                "last_updated": current_time_utc,
                "message": "Person Created Successfuly"
            }
    
    return response_json

@app.get("/api")
async def get_person(db: db_dependency):
    persons = db.query(models.Persons).all()

    return persons

@app.get('/api/{user}')
async def get_person(db: db_dependency, user):
    if user.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user.lower()).first()
    

    if not person:
        raise HTTPException(status_code=404, detail="user not in database")
    
    response_json = {
                "id": person.id,
                "name": person.name                
            }
    
    return response_json

@app.patch("/api/{user}")
async def update_person(updated_person: schemas.PersonBase,   db: db_dependency, user):
    if user.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user.lower()).first()

    if not person:
        raise HTTPException(status_code=404, detail="user not in database")
    
    old_name = person.name
    person.name = updated_person.name.lower()
    db.commit()

    current_time_utc = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    response_json = {
                "name": person.name,
                "last_updated": current_time_utc,
                "message": f"Name updated to {person.name} successfuly"
            }
    
    return response_json

@app.delete("/api/{user}", status_code=200)
async def delete_person(db:db_dependency, user):
    if user.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user.lower()).first()

    if not person:
        raise HTTPException(status_code=404, detail="user not in database")
    
    db.delete(person)
    db.commit()

    response_json = {
                        "message": "Deleted successfully"
                    }
    
    return response_json