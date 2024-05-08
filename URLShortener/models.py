from pydantic import BaseModel

class Site(BaseModel):
    hash: str = None
    redirect: str
