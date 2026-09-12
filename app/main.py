from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import Base, engine, get_db


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Contacts API",
    description="REST API для управління контактами",
    version="1.0.0",
)


@app.get(
    "/",
    tags=["Health"],
)
def read_root() -> dict[str, str]:
    return {
        "message": "Contacts API is running",
    }


@app.get(
    "/contacts",
    response_model=list[schemas.ContactResponse],
    tags=["Contacts"],
)
def read_contacts(
    skip: int = Query(
        default=0,
        ge=0,
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=100,
    ),
    search: str | None = Query(
        default=None,
        min_length=1,
    ),
    db: Session = Depends(get_db),
) -> list[models.Contact]:
    return crud.get_contacts(
        db=db,
        skip=skip,
        limit=limit,
        search=search,
    )


@app.get(
    "/contacts/{contact_id}",
    response_model=schemas.ContactResponse,
    tags=["Contacts"],
)
def read_contact(
    contact_id: int,
    db: Session = Depends(get_db),
) -> models.Contact:
    contact = crud.get_contact(
        db=db,
        contact_id=contact_id,
    )

    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found",
        )

    return contact


@app.post(
    "/contacts",
    response_model=schemas.ContactResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Contacts"],
)
def create_contact(
    contact_data: schemas.ContactCreate,
    db: Session = Depends(get_db),
) -> models.Contact:
    existing_contact = crud.get_contact_by_email(
        db=db,
        email=str(contact_data.email),
    )

    if existing_contact is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A contact with this email already exists",
        )

    try:
        return crud.create_contact(
            db=db,
            contact_data=contact_data,
        )
    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A contact with this email already exists",
        )


@app.patch(
    "/contacts/{contact_id}",
    response_model=schemas.ContactResponse,
    tags=["Contacts"],
)
def update_contact(
    contact_id: int,
    contact_data: schemas.ContactUpdate,
    db: Session = Depends(get_db),
) -> models.Contact:
    contact = crud.get_contact(
        db=db,
        contact_id=contact_id,
    )

    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found",
        )

    if contact_data.email is not None:
        existing_contact = crud.get_contact_by_email(
            db=db,
            email=str(contact_data.email),
        )

        if (
            existing_contact is not None
            and existing_contact.id != contact_id
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A contact with this email already exists",
            )

    try:
        return crud.update_contact(
            db=db,
            contact=contact,
            contact_data=contact_data,
        )
    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A contact with this email already exists",
        )


@app.delete(
    "/contacts/{contact_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Contacts"],
)
def delete_contact(
    contact_id: int,
    db: Session = Depends(get_db),
) -> None:
    contact = crud.get_contact(
        db=db,
        contact_id=contact_id,
    )

    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found",
        )

    crud.delete_contact(
        db=db,
        contact=contact,
    )