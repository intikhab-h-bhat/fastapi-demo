
from sqlalchemy.orm import Session
from .. import models, schemas





def create_user(request: schemas.User, db: Session):
    
    new_user=models.User(name=request.name,email=request.email,password=Hash.hashed(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

  


def get_all(db: Session):

    allusers = db.query(models.User).all()
    if not allusers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")

    return allusers


