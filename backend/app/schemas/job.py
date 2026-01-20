from typing import Optional
from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    raw_description: str
    company: Optional[str] = None
    location: Optional[str] = None
    source: Optional[str] = None
    source_url: Optional[str] = None