from typing import List, Optional
from uuid import uuid4, UUID
from pydantic import BaseModel, Field, EmailStr


class PlanModel(BaseModel):
    plan: str
    amount: int


class AddonsModel(BaseModel):
    addon: str
    amount: int


class FormModel(BaseModel):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    name: str = Field(...)
    email: EmailStr() = Field(...)
    phone: str = Field(...)
    billing: str = Field(...)
    subscription: PlanModel = Field(...)
    add_ons: List[AddonsModel] | List

    class Config:
        populate_by_name = True
