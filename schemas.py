from pydantic import BaseModel

class CaesarModel(BaseModel):
    text: str
    offset: int
    mode: str

class FenceModel(BaseModel):
    text: str