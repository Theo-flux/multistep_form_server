from typing import List, Optional
from uuid import uuid5
from pydantic import BaseModel, Field, EmailStr


class PlanModel(BaseModel):
    plan: str
    amount: int


class AddonsModel(BaseModel):
    addon: str
    description: str
    amount: int


class FormModel(BaseModel):
    id: str = Field(default_factory=uuid5, alias="_id")
    name: str = Field(...)
    email: EmailStr()
    billing: str = Field(...)
    subscription: PlanModel = Field(...)
    add_ons: List[AddonsModel] | List
