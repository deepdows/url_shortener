from secrets import token_hex

from fastapi import HTTPException, status

from .models import ShortenedURL


def to_camel(string: str) -> str:
    words = string.split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])


def check_if_exists(url_path, db):
    if db.query(ShortenedURL).filter_by(url_path=url_path).first():
        return True
    return False


def add_to_db(url, url_path, db):
    new_url = ShortenedURL(url=url, url_path=url_path)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url


def create_url_path(url, db):
    url_path = token_hex(3)
    i, LIMIT = 0, 30
    while check_if_exists(url_path, db):
        i += 1
        if i > LIMIT:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Can't find url for you, try again",
            )
    return add_to_db(url, url_path, db)


def create_custom_url(url, custom_url_path, db):
    if check_if_exists(custom_url_path, db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="This URL already exists"
        )
    return add_to_db(url, custom_url_path, db)


def get_url_from_path(url_path, db):
    response = db.query(ShortenedURL).filter_by(url_path=url_path).first()
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="URL not found"
        )
    return response


def validate_url_length(url, min, max, name):
    if len(url) > max:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"{name} is too long, maximum length is {max}"
        )
    if len(url) < min:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"{name} is too short, minimum length is {min}"
        )