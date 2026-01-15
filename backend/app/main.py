from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(title="FitCraft API", version="0.1.0")
app.include_router(api_router)

@app.get("/health")
def health():
    return {"status": "ok"}