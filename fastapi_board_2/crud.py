from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import desc, asc 
from models import Post
from schemas import PostCreate
from fastapi import HTTPException

async def create_post(db:AsyncSession, post: PostCreate) -> Post:
    new_post = Post(title=post.title, content=post.content)
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post

async def get_posts(db:AsyncSession, skip: int = 0, limit:int =10, order:str ="asc", sort_by:str="id"):
    allowed_sort_fields = ["id","created_at","title"]
    if sort_by not in allowed_sort_fields:
        raise HTTPException(status_code=400, detail=f"불가능한 정렬 조건 입니다.: {allowed_sort_fields}")
    
    sort_field = getattr(Post,sort_by)

    if order == "desc":
        order_by = desc(sort_field)
    else:
        order_by = asc(sort_field)

    result = await db.execute(select(Post).order_by(order_by).offset(skip).limit(limit))

    return result.scalars().all()

async def get_post(db: AsyncSession, post_id: int):
    result = await db.execute(select(Post).where(Post.id == post_id))
    return result.scalar_one_or_none()


async def update_post(db: AsyncSession, post_id: int, updated_post:PostCreate) -> Post:
    post = await get_post(db, post_id)
    if post:
        post.title = updated_post.title
        post.content = updated_post.content
        db.add(post)
        await db.commit()
        await db.refresh(post)
    return post


async def delete_post(db: AsyncSession, post_id:int) -> bool:
    post = await get_post(db,post_id)
    if post:
        await db.delete(post)
        await db.commit()
        return True
    return False
