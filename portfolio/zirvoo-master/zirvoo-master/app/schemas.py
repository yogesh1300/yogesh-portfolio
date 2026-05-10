from datetime import date
from enum import Enum
from typing import Annotated, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, PositiveFloat


class RoleEnum(str, Enum):
    viewer = "viewer"
    analyst = "analyst"
    admin = "admin"


UsernameType = Annotated[str, Field(json_schema_extra={"strip_whitespace": True}, min_length=3, max_length=50)]
PasswordType = Annotated[str, Field(json_schema_extra={"strip_whitespace": True}, min_length=6, max_length=128)]
TxType = Literal["income", "expense"]
CategoryType = Annotated[str, Field(json_schema_extra={"strip_whitespace": True}, min_length=2, max_length=50)]


class UserBase(BaseModel):
    username: UsernameType
    role: RoleEnum = RoleEnum.viewer


class UserCreate(UserBase):
    password: PasswordType


class UserRead(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class TransactionBase(BaseModel):
    amount: PositiveFloat
    type: TxType
    category: CategoryType
    date: date
    notes: Optional[str] = ""


class TransactionCreate(TransactionBase):
    owner_id: int


class TransactionUpdate(BaseModel):
    amount: Optional[PositiveFloat] = None
    type: Optional[TxType] = None
    category: Optional[CategoryType] = None
    date: Optional[date] = None
    notes: Optional[str] = None


class TransactionRead(TransactionBase):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class SummaryResponse(BaseModel):
    total_income: float
    total_expense: float
    balance: float
    category_breakdown: dict
    monthly_totals: dict
    recent_activity: List[TransactionRead] = []


class TransactionFilterParams(BaseModel):
    type: Optional[TxType] = Field(None, pattern="^(income|expense)$")
    category: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    owner_id: Optional[int] = None
