from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app= FastAPI()


@app.get("/")
def index():
    return {"data":'blog list'}

@app.get("/blog/comments")
def unpublished():
    return {"data":'unpublished blog'}

@app.get("/blog/published")
def published(limit:int=10,published:bool=True,sort:Optional[str]=None):
 
    if published:
        return {"data":'published blog'}
    else:
        return {"data":'unpublished blog'}
   

@app.get("/blog/{id}")
def show(id:int):
        return {"data":id}


class Blog(BaseModel):
    title:str
    content:str
    published:Optional[bool]=True

@app.post("/blog")
def post(request:Blog):

    return {"data":f'creating blog with title {request}'}

