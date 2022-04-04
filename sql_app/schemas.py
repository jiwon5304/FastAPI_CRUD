from typing import List, Optional
from pydantic import BaseModel

## Pydantic models
# Django의 serializer와 유사 : api에서 데이터를 반환할 때
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class ItemDelete(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str




class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True