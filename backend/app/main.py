from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes import router as api_router
from app.db.session import init_db



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield
    # Shutdown

app = FastAPI(
    title="FitCraft API",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(api_router)

@app.get("/health")
def health():
    return {"status": "ok"}
