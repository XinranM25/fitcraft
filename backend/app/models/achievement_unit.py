from typing import Optional
from sqlmodel import SQLModel, Field

class AchievementUnit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(index=True, unique=True)
    title: str
    description: Optional[str] = None