

from fastapi import APIRouter, Depends, HTTPException, status,Response
from sqlalchemy.orm import Session
from typing import List
from .. import schemas,database,models
from ..hashing import Hash
from ..repository import user as user_repo


router = APIRouter(
    prefix="/user",
    tags=["users"]
    
)


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser,tags=["users"])
def create_user(request:schemas.User,db:Session=Depends(database.get_db)): 
    new_user=user_repo.create_user(request,db)   
    return new_user

   
    

@router.get("/shoWallusers", response_model=List[schemas.ShowUser])
def get_all_user(db:Session=Depends(database.get_db)):
   all_users=user_repo.get_all(db)
   return all_users