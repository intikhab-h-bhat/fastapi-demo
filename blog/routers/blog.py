

from fastapi import APIRouter, Depends, HTTPException, status,Response
from sqlalchemy.orm import Session
from typing import List
from .. import schemas,database


router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
    
)



@router.post("/blog", status_code=status.HTTP_201_CREATED,response_model=schemas.ShowBlog)
def create_blog(request: schemas.Blog, db:Session =Depends(database.get_db)):
    new_blog=models.Blog(title=request.title, body=request.body, published=request.published, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)    

    return new_blog



@router.get("/all",response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db)):
    
    blogs = db.query(models.Blog).all()

    return blogs


@router.get("/blog/{id}", status_code=200)
def get_blog_by_id(id:int, response:Response,db:Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"error":"blog not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")

    return blog

@router.delete("/blog/{id}")
def delet_blog(id:int,db:Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        return {"error":"blog not found"}
    title=blog.title
    db.delete(blog)
    db.commit()
    return {"message":f"blog with {title} deleted successfully"}


@router.put("/blog/{id}")
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

