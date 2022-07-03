from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from database_init import Base
from url_shortener.router import router as url_shortener

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener", docs_url="/api/docs", redoc_url=None, openapi_url="/api/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(url_shortener, prefix="/api")
