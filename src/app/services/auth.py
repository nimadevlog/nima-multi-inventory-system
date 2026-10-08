import asyncio

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password
from app.db.models.user import User
from app.domain.exceptions import EmailAlreadyRegisteredError
from app.repositories.user import UserRepository


class AuthService:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._users = UserRepository(session)

    async def register(self, email: str, password: str) -> User:
        normalized_email = email.strip().lower()

        if await self._users.get_by_email(normalized_email) is not None:
            raise EmailAlreadyRegisteredError

        password_hash = await asyncio.to_thread(hash_password, password)
        user = User(email=normalized_email, password_hash=password_hash)

        try:
            await self._users.add(user)
            await self._session.commit()
        except IntegrityError:
            await self._session.rollback()
            raise EmailAlreadyRegisteredError from None

        return user
