from sqlalchemy.orm import Session
from .. import models




def create_blog(request,db:Session):
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
    return blog

def delete_blog(id:int,db:Session):
    blog=get_blog_by_id(id,db)
    title=blog.title
    db.delete(blog)
    db.commit()
    return {"message":f"blog with {title} deleted successfully"}

  
