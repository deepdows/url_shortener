from typing import Optional

from pydantic import BaseModel

from .services import to_camel

class URLBase(BaseModel):
    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True

class CreateURL(URLBase):
    url: str
    custom_path_url: Optional[str] = None

class ReturnURLPath(URLBase):
    url_path: str

class ReturnURL(URLBase):
    url: str