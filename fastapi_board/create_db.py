import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine, Base
from models import Post

async def init_db():
    async with engine.begin() as conn:
        # 모든 테이블 생성 
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_db())