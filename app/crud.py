from sqlalchemy import or_, select
from sqlalchemy.orm import Session
from datetime import date, timedelta

from . import models, schemas


def get_contact(
    db: Session,
    contact_id: int,
) -> models.Contact | None:
    statement = select(models.Contact).where(
        models.Contact.id == contact_id
    )

    return db.scalar(statement)


def get_contacts(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    search: str | None = None,
) -> list[models.Contact]:
    statement = select(models.Contact)

    if search:
        search_pattern = f"%{search}%"

        statement = statement.where(
            or_(
                models.Contact.first_name.ilike(search_pattern),
                models.Contact.last_name.ilike(search_pattern),
                models.Contact.email.ilike(search_pattern),
                models.Contact.company.ilike(search_pattern),
            )
        )

    statement = (
        statement
        .order_by(models.Contact.id)
        .offset(skip)
        .limit(limit)
    )

    return list(db.scalars(statement).all())


def get_contact_by_email(
    db: Session,
    email: str,
) -> models.Contact | None:
    statement = select(models.Contact).where(
        models.Contact.email == email
    )

    return db.scalar(statement)


def create_contact(
    db: Session,
    contact_data: schemas.ContactCreate,
) -> models.Contact:
    contact = models.Contact(
        **contact_data.model_dump()
    )

    db.add(contact)
    db.commit()
    db.refresh(contact)

    return contact


def update_contact(
    db: Session,
    contact: models.Contact,
    contact_data: schemas.ContactUpdate,
) -> models.Contact:
    update_data = contact_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(contact, field, value)

    db.commit()
    db.refresh(contact)

    return contact


def delete_contact(
    db: Session,
    contact: models.Contact,
) -> None:
    db.delete(contact)
    db.commit()
    
def get_upcoming_birthdays(
    db: Session,
) -> list[models.Contact]:
    today = date.today()
    end_date = today + timedelta(days=7)

    contacts = db.scalars(
        select(models.Contact)
        .where(models.Contact.birth_date.is_not(None))
        .order_by(models.Contact.birth_date)
    ).all()

    upcoming_contacts = []

    for contact in contacts:
        birthday = contact.birth_date.replace(
            year=today.year
        )

        if birthday < today:
            birthday = birthday.replace(
                year=today.year + 1
            )

        if today <= birthday <= end_date:
            upcoming_contacts.append(contact)

    return upcoming_contacts