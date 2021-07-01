from sqlalchemy import Column, DateTime, Integer, String, func

from src import database


class JigasyaMember(database.Base):
    __tablename__ = 'jigasya_members'

    telegram_id = Column(
        Integer, primary_key=True, autoincrement=False, index=True,
    )
    username = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
