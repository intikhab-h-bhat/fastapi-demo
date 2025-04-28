from pydantic import BaseModel




class BaseBlog(BaseModel):
    title: str
    body: str
    published: bool = True

  

class Blog(BaseBlog):
    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list[Blog] = []
    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    creator: ShowUser

    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str
   

