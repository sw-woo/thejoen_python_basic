from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./bulletin_board.db"

# 엔진 생성
engine = create_async_engine(
    DATABASE_URL, echo=True
)

# 세션 로컬 클래스 생성
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

#기본 클래스 생성 
Base = declarative_base()


#의존성 주입을 위한 함수 
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
