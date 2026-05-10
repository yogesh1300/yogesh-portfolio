from datetime import timedelta

from fastapi import Depends, FastAPI, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List

from . import crud, schemas
from .database import Base, SessionLocal, engine
from .dependencies import require_role
from .security import ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user, create_access_token

app = FastAPI(
    title="Zorvyn Finance System Backend",
    description="A FastAPI backend for personal finance tracking with role-based access control.",
    version="1.0.0",
)


# Initialize the database
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup_event():
    try:
        db = SessionLocal()
        if not crud.get_user_by_username(db, "admin"):
            crud.create_user(db, schemas.UserCreate(username="admin", role=schemas.RoleEnum.admin, password="admin123"))
        if not crud.get_user_by_username(db, "analyst"):
            crud.create_user(db, schemas.UserCreate(username="analyst", role=schemas.RoleEnum.analyst, password="analyst123"))
        if not crud.get_user_by_username(db, "viewer"):
            crud.create_user(db, schemas.UserCreate(username="viewer", role=schemas.RoleEnum.viewer, password="viewer123"))
        db.close()
    except Exception as e:
        # Silently handle startup errors (e.g., in test environments)
        pass


@app.post("/users", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db), _=Depends(require_role(schemas.RoleEnum.admin))):
    if crud.get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    return crud.create_user(db, user)


@app.get("/users", response_model=List[schemas.UserRead])
def list_users(db: Session = Depends(get_db), _=Depends(require_role(schemas.RoleEnum.admin))):
    return crud.get_users(db)


@app.post("/token")
def login_for_access_token(
    username: str = Query(...),
    password: str = Query(...),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/transactions", response_model=schemas.TransactionRead, status_code=status.HTTP_201_CREATED)
def create_transaction(tx: schemas.TransactionCreate, db: Session = Depends(get_db), _=Depends(require_role(schemas.RoleEnum.admin, schemas.RoleEnum.analyst))):
    try:
        return crud.create_transaction(db, tx)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.get("/transactions", response_model=List[schemas.TransactionRead])
def list_transactions(
    type: str = Query(None, pattern="^(income|expense)$"),
    category: str = Query(None),
    start_date: str = Query(None),
    end_date: str = Query(None),
    owner_id: int = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
    _=Depends(require_role(schemas.RoleEnum.viewer, schemas.RoleEnum.analyst, schemas.RoleEnum.admin)),
):
    filters = schemas.TransactionFilterParams(type=type, category=category, start_date=start_date, end_date=end_date, owner_id=owner_id)
    return crud.get_transactions(db, filters, skip=skip, limit=limit)


@app.get("/transactions/{transaction_id}", response_model=schemas.TransactionRead)
def get_transaction(transaction_id: int, db: Session = Depends(get_db), _=Depends(require_role(schemas.RoleEnum.viewer, schemas.RoleEnum.analyst, schemas.RoleEnum.admin))):
    tx = crud.get_transaction(db, transaction_id)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx


@app.put("/transactions/{transaction_id}", response_model=schemas.TransactionRead)
def update_transaction(transaction_id: int, tx_update: schemas.TransactionUpdate, db: Session = Depends(get_db), _=Depends(require_role(schemas.RoleEnum.admin, schemas.RoleEnum.analyst))):
    tx = crud.update_transaction(db, transaction_id, tx_update)
    if tx is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx


@app.delete("/transactions/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_transaction(transaction_id: int, db: Session = Depends(get_db), _=Depends(require_role(schemas.RoleEnum.admin))):
    removed = crud.delete_transaction(db, transaction_id)
    if not removed:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return None


@app.get("/summary", response_model=schemas.SummaryResponse)
def get_summary(
    type: str = Query(None, pattern="^(income|expense)$"),
    category: str = Query(None),
    start_date: str = Query(None),
    end_date: str = Query(None),
    owner_id: int = Query(None),
    db: Session = Depends(get_db),
    _=Depends(require_role(schemas.RoleEnum.viewer, schemas.RoleEnum.analyst, schemas.RoleEnum.admin)),
):
    filters = schemas.TransactionFilterParams(type=type, category=category, start_date=start_date, end_date=end_date, owner_id=owner_id)
    return crud.build_summary(db, filters)
