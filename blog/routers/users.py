

from fastapi import APIRouter, Depends, HTTPException, status,Response
from sqlalchemy.orm import Session
from typing import List
from .. import schemas,database,models
from ..hashing import Hash




router = APIRouter(
    prefix="/user",
    tags=["users"]
    
)


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser,tags=["users"])
def create_user(request:schemas.User,db:Session=Depends(database.get_db)):

  

    new_user=models.User(name=request.name,email=request.email,password=Hash.hashed(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
    

@router.get("/shoallusers", response_model=List[schemas.ShowUser],tags=["users"])
def get_all_user(db:Session=Depends(database.get_db)):
    allusers = db.query(models.User).all()
    if not allusers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")

    return allusers