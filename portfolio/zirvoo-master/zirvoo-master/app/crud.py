from datetime import date
from typing import Any, Dict, List, Optional

from sqlalchemy.orm import Session

from . import models, schemas
from .security import get_password_hash


# User CRUD

def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).order_by(models.User.id).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, role=user.role.value, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Transaction CRUD

def get_transaction(db: Session, transaction_id: int) -> Optional[models.Transaction]:
    return db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()


def get_transactions(db: Session, filters: schemas.TransactionFilterParams, skip: int = 0, limit: int = 200) -> List[models.Transaction]:
    query = db.query(models.Transaction)

    if filters.owner_id is not None:
        query = query.filter(models.Transaction.owner_id == filters.owner_id)
    if filters.type is not None:
        query = query.filter(models.Transaction.type == filters.type)
    if filters.category is not None:
        query = query.filter(models.Transaction.category.ilike(f"%{filters.category}%"))
    if filters.start_date is not None:
        query = query.filter(models.Transaction.date >= filters.start_date)
    if filters.end_date is not None:
        query = query.filter(models.Transaction.date <= filters.end_date)

    return query.order_by(models.Transaction.date.desc()).offset(skip).limit(limit).all()


def create_transaction(db: Session, tx: schemas.TransactionCreate) -> models.Transaction:
    if not get_user(db, tx.owner_id):
        raise ValueError("owner_id does not exist")

    transaction = models.Transaction(
        amount=tx.amount,
        type=tx.type,
        category=tx.category,
        date=tx.date,
        notes=tx.notes or "",
        owner_id=tx.owner_id,
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


def update_transaction(db: Session, transaction_id: int, tx_update: schemas.TransactionUpdate) -> Optional[models.Transaction]:
    transaction = get_transaction(db, transaction_id)
    if transaction is None:
        return None

    for field, value in tx_update.dict(exclude_unset=True).items():
        setattr(transaction, field, value)

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


def delete_transaction(db: Session, transaction_id: int) -> bool:
    transaction = get_transaction(db, transaction_id)
    if not transaction:
        return False
    db.delete(transaction)
    db.commit()
    return True


def build_summary(db: Session, filters: schemas.TransactionFilterParams) -> schemas.SummaryResponse:
    transactions = get_transactions(db, filters, skip=0, limit=1000)
    total_income = sum(tx.amount for tx in transactions if tx.type == "income")
    total_expense = sum(tx.amount for tx in transactions if tx.type == "expense")
    balance = total_income - total_expense

    category_breakdown: Dict[str, float] = {}
    monthly_totals: Dict[str, Dict[str, float]] = {}

    for tx in transactions:
        category_breakdown.setdefault(tx.category, 0.0)
        category_breakdown[tx.category] += tx.amount if tx.type == "income" else -tx.amount

        month_key = tx.date.strftime("%Y-%m")
        month_data = monthly_totals.setdefault(month_key, {"income": 0.0, "expense": 0.0})
        if tx.type == "income":
            month_data["income"] += tx.amount
        else:
            month_data["expense"] += tx.amount

    recent_activity = transactions[:10]

    return schemas.SummaryResponse(
        total_income=total_income,
        total_expense=total_expense,
        balance=balance,
        category_breakdown=category_breakdown,
        monthly_totals=monthly_totals,
        recent_activity=recent_activity,
    )