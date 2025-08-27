from .. import models, schemas, utils
from fastapi import Body, FastAPI, HTTPException, Response, status, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from .. import oauth2
from typing import List, Optional
from sqlalchemy import func

router =  APIRouter(prefix="/posts", tags=["Posts"])



# Create
@router.post("/", status_code=status.HTTP_201_CREATED, response_model = schemas.Post)
def create_post(post: schemas.PostCreate, 
                db: Session = Depends(get_db), 
                current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    print(current_user.id)
    new_post = models.Post(owner_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

### READ
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), 
              limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # if posts.owner_id != current_user.id:
    #      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    
    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
         models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return results


@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: str, db: Session = Depends(get_db)):
        post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
         models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
        if not post:
            raise HTTPException(detail="This post does not exist.", status_code=404)
        
        # if post.owner_id != current_user.id:
        #  raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
        return post


    
### UPDATE
@router.put("/{id}", response_model= schemas.Post)
def get_update(id: str, post: schemas.PostCreate, db: Session=Depends(get_db), 
               current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    if not post_query.first():
        raise HTTPException(detail="This data does not exist.", status_code=404)
    
    if post_query.first().owner_id != current_user.id:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()

### DELETE
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def get_delete(id:str, db: Session = Depends(get_db), 
               current_user: schemas.TokenData = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(detail="This data does not exist.", status_code=404)
    
    if post.first().owner_id != current_user.id:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    
    post.delete(synchronize_session=False)
    db.commit()