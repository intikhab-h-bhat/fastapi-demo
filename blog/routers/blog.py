

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
    
   

@router.get("/blog/{id}", status_code=200)
def get_blog_by_id(id:int, response:Response,db:Session=Depends(database.get_db)):
    blog=blog_repo.get_blog_by_id(id,db)
    if not blog:       
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    return blog

@router.delete("/{id}")
def delet_blog(id:int,db:Session=Depends(database.get_db)):
    blog=blog_repo.get_blog_by_id(id,db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    delblog=blog_repo.delete_blog(id,db)
    return delblog
     

@router.put("/{id}")
def update_blog(id:int,request:schemas.Blog,db:Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
    
    blog.title=request.title
    blog.body=request.body
    blog.published=request.published
    # blog.update(request)
    db.commit()
    return "updated successfully"

