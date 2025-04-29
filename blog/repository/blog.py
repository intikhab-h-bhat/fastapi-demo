from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status





def create_blog(request:schemas,db:Session):
    new_blog=models.Blog(title=request.title, body=request.body, published=request.published, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)    

    return new_blog



def get_all(db: Session):
     blogs = db.query(models.Blog).all()
     return blogs

def get_blog_by_id(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:       
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    return blog


def delete_blog(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    title=blog.title
    db.delete(blog)
    db.commit()
    return {"message":f"blog with {title} deleted successfully"}

  
def update_blog(id:int,request,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")

    blog.title=request.title
    blog.body=request.body
    blog.published=request.published
    db.commit()
    return "updated successfully"