from fastapi import FastAPI, Depends, HTTPException , Query
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from schemas import PostCreate, PostResponse
from crud import create_post ,get_posts, get_post, update_post, delete_post
from database import get_db

# fastapi web 객체 생성
app = FastAPI()

#http://127.0.0.1:8000/
#method: get (read)

@app.get("/") 
async def read_root():
    return {"message":"FastAPI 게시판에 오신 것을 환영합니다! 오늘은 fast api 게시판을 만들어 볼겁니다."}


#http://127.0.0.1:8000/posts/
#method: post (create)

@app.post("/posts/", response_model=PostResponse)
async def create_new_post(post: PostCreate, db:AsyncSession = Depends(get_db)):
    return await create_post(db, post)

#쿼리 파라메터 방식
#http://127.0.0.1:8000/posts/?skip=0&limit=10&order=asc&sort_by=id
#method: get (read)
@app.get("/posts/", response_model=List[PostResponse])
async def read_all_posts(
    skip: int = 0,
    limit: int = 10,
    order: Optional[str] = Query("asc",regex="^(asc|desc)$"),
    sort_by: Optional[str]= Query("id",regex="^(id|created_at|title)$"),
    db: AsyncSession = Depends(get_db)
):
    posts = await get_posts(db, skip=skip, limit=limit, order=order, sort_by=sort_by)
    return posts

#와일드 카드 방식
#http://127.0.0.1:8000/posts/1
#method: get (read)

@app.get("/posts/{post_id}", response_model=PostResponse)
async def update_existing_post(post_id: int, db : AsyncSession =Depends(get_db)):
    post = await get_post(db,post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="게시물을 찾울 수 없습니다.")
    return post

#와일드 카드 방식
#metod : put
@app.put("/posts/{post_id}",response_model=PostResponse)
async def update_existing_post(post_id: int, updated_post: PostCreate, db:AsyncSession = Depends(get_db)):
    post = await update_post(db, post_id, updated_post)
    if post is None:
        raise HTTPException(status_code=404, detail="게시물을 찾을 수 없습니다.")
    return post

#method : delete 
@app.delete("/posts/{post_id}", response_model=dict)
async def delete_existing_post(post_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_post(db, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="게시물을 찾울 수 없습니다.")
    return {"detail":"게시물이 삭제되었습니다."}

