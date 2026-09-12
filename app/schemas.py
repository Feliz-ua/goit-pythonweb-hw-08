from datetime import datetime
from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ContactBase(BaseModel):
    first_name: str = Field(
        min_length=1,
        max_length=100,
    )

    last_name: str = Field(
        min_length=1,
        max_length=100,
    )

    email: EmailStr
    
    birth_date: date | None = None

    phone: str | None = Field(
        default=None,
        max_length=30,
    )

    company: str | None = Field(
        default=None,
        max_length=150,
    )

    notes: str | None = Field(
        default=None,
        max_length=1000,
    )


class ContactCreate(ContactBase):
    pass


class ContactUpdate(BaseModel):
    first_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    last_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    email: EmailStr | None = None
    
    birth_date: date | None = None

    phone: str | None = Field(
        default=None,
        max_length=30,
    )

    company: str | None = Field(
        default=None,
        max_length=150,
    )

    notes: str | None = Field(
        default=None,
        max_length=1000,
    )


class ContactResponse(ContactBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)