from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.achievement_unit import AchievementUnit
from app.models.job import Job
from app.schemas.job import JobCreate

router = APIRouter(prefix="/api")


@router.get("/ping")
def ping():
    return {"message": "pong"}


@router.post("/aus/seed")
def seed_aus(session: Session = Depends(get_session)):
    items = [
        AchievementUnit(code="AU_02", title="Performance evaluation", description="Real + simulated data validation"),
        AchievementUnit(code="AU_03", title="Optimization & scenario analysis", description="LCOE / scenario optimization"),
        AchievementUnit(code="AU_04", title="Research modeling", description="Modeling + documentation"),
        AchievementUnit(code="AU_05", title="Time-series experiments", description="Experimental / time-series analysis"),
        AchievementUnit(code="AU_07", title="Stakeholders & collaboration", description="Cross-functional ownership"),
    ]

    existing = {au.code for au in session.exec(select(AchievementUnit)).all()}
    for it in items:
        if it.code not in existing:
            session.add(it)

    session.commit()
    return {"seeded": len(items), "already_existing": len(existing)}


@router.get("/aus")
def list_aus(session: Session = Depends(get_session)):
    aus = session.exec(select(AchievementUnit)).all()
    return {"items": aus}


@router.post("/jobs", response_model=Job)
def create_job(payload: JobCreate, session: Session = Depends(get_session)):
    job = Job(**payload.model_dump())
    session.add(job)
    session.commit()
    session.refresh(job)
    return job


@router.get("/jobs", response_model=list[Job])
def list_jobs(session: Session = Depends(get_session)):
    statement = select(Job).order_by(Job.id.desc())
    jobs = session.exec(statement).all()
    return jobs


@router.get("/jobs/{job_id}", response_model=Job)
def get_job(job_id: int, session: Session = Depends(get_session)):
    job = session.get(Job, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job