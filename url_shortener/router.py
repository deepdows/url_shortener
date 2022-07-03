from database_init import get_db
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .schemas import CreateURL, ReturnURLPath, ReturnURL
from .services import create_custom_url, create_url_path, get_url_from_path, validate_url_length

router = APIRouter(prefix="/shorten", tags=["Shorten"])


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_url(data: CreateURL, db: Session = Depends(get_db)):
    validate_url_length(data.url, min=1, max=256, name="URL")
    if data.custom_path_url:
        validate_url_length(data.custom_path_url, min=4, max=10, name="URL path")
        response = create_custom_url(data.url, data.custom_path_url, db)
    else:
        response = create_url_path(data.url, db)
    return ReturnURLPath.from_orm(response)


@router.get("/{url_path}", status_code=status.HTTP_200_OK)
async def get_url(url_path: str, db: Session = Depends(get_db)):
    response = get_url_from_path(url_path, db)
    return ReturnURL.from_orm(response)
