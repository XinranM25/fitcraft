from typing import Optional
from sqlmodel import SQLModel, Field
from app.core.taxonomy import JobArchtype


class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    company: Optional[str] = None
    location: Optional[str] = None
    source: Optional[str] = None
    source_url: Optional[str] = None
    raw_description: str
    archetype: JobArchtype = Field(default=JobArchtype.APPLIED__ENERGY_ANALYTIC)
    