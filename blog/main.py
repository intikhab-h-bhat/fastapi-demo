from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import models
from .database import engine




from .routers import blog,users




app=FastAPI()

models.Base.metadata.create_all(bind=engine)



app.include_router(blog.router)
app.include_router(users.router)





# pass_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

