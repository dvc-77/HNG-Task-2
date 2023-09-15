from sqlalchemy.orm import Session
import models, schemas
from fastapi import Path, HTTPException

#Creating the endpoint to add a new person
def create_person(person: schemas.PersonBase, db: Session):
    db_person = models.Persons(name=person.name.lower())
    db.add(db_person)
    db.commit()
    
def get_person(db: Session, user):
    if user.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user.lower()).first()
    

    if not person:
        raise HTTPException(status_code=404, detail="user not available")
    
    return person

def update_person(updated_person: schemas.PersonBase,   db: Session, user):
    if user.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user.lower()).first()

    if not person:
        raise HTTPException(status_code=404, detail="user not available")
    
    person.name = updated_person.name.lower()
    db.commit()

def delete_person(db:Session, user):
    if user.isdigit():
        person = db.query(models.Persons).filter(models.Persons.id == int(user)).first()
    else:
        person = db.query(models.Persons).filter(models.Persons.name == user.lower()).first()

    if not person:
        raise HTTPException(status_code=404, detail="user not available")
    
    db.delete(person)
    db.commit()