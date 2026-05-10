from typing import Optional

from fastapi import Depends, Header, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from . import crud
from .database import SessionLocal
from .schemas import RoleEnum
from .security import ALGORITHM, SECRET_KEY


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_role(
    x_user_role: Optional[str] = Header(None, alias="X-User-Role"),
    authorization: Optional[str] = Header(None, alias="Authorization"),
    db: Session = Depends(get_db),
) -> RoleEnum:
    if x_user_role:
        try:
            return RoleEnum(x_user_role.lower())
        except ValueError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid role header (X-User-Role). allowed: viewer, analyst, admin",
            )

    if authorization:
        token_type, _, token = authorization.partition(" ")
        if token_type.lower() != "bearer" or not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authorization header. Use Bearer <token>",
            )

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise JWTError("missing subject")
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )

        user = crud.get_user_by_username(db, username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User does not exist",
            )

        return RoleEnum(user.role)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Missing role header (X-User-Role) or Authorization bearer token",
    )


def require_role(*allowed_roles: RoleEnum):
    def role_checker(current_role: RoleEnum = Depends(get_current_role)) -> RoleEnum:
        if current_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Operation not permitted for role '{current_role}'. required: {[r.value for r in allowed_roles]}",
            )
        return current_role

    return role_checker