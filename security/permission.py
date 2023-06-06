from datetime import datetime, timedelta
import jwt
import os
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt


class TokenPayload(BaseModel):
    exp: str
    sub: str
    namespaces: str


def generate_token(username, isAdmin) -> str:
    expire = datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
    to_encode = {"exp": expire, "sub": username, "namespaces": "admin_role" if isAdmin else "user_role"}
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm="HS256")

    return encoded_jwt


async def get_token_payload(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> TokenPayload:
    try:
        token = credentials.credentials
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        token_data = TokenPayload(**payload)
        return token_data
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def is_authenticated(token_data: TokenPayload = Depends(get_token_payload)):
    try:
        if "exp" in token_data and token_data["exp"] < time.time():
            raise ValueError("Token has expired")

        return token_data
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def is_admin(token_data: TokenPayload = Depends(is_authenticated)):
    if token_data.namespaces != "admin_role":
        raise HTTPException(status_code=403, detail="You are not an admin")

    return token_data
