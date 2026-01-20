from sqlmodel import SQLModel, Session, create_engine
from app.db.settings import settings

engine = create_engine(settings.database_url, echo=False)

def init_db() -> None:
    from app.models.achievement_unit import AchievementUnit
    from app.models.job import Job
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

        