

from fastapi import APIRouter, Depends, HTTPException, status,Response
from sqlalchemy.orm import Session
from typing import List
from .. import schemas,database,models

from ..repository import blog as blog_repo


router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
    
)



@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.ShowBlog)
def create_blog(request: schemas.Blog, db:Session =Depends(database.get_db)):
    new_blog=blog_repo.create_blog(request,db)   
    return new_blog



@router.get("/all",response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db)):
    return blog_repo.get_all(db)
    
   

@router.get("/{id}", status_code=200)
def get_blog_by_id(id:int, response:Response,db:Session=Depends(database.get_db)):
    blog=blog_repo.get_blog_by_id(id,db)    
    return blog

@router.delete("/{id}")
def delete_blog(id:int,db:Session=Depends(database.get_db)):
    delblog=blog_repo.delete_blog(id,db)
    return delblog
     

@router.put("/{id}")
def update_blog(id:int,request:schemas.Blog,db:Session=Depends(database.get_db)):
    update_blog=blog_repo.update_blog(id,request,db)   
    return update_blog

