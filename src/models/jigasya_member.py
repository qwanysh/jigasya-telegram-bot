from datetime import datetime

from sqlalchemy import Column, Date, DateTime, Integer, String, event, func

from src import database


class JigasyaMember(database.Base):
    __tablename__ = 'jigasya_members'

    telegram_id = Column(
        Integer, primary_key=True, autoincrement=False, index=True,
    )
    username = Column(String)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    birth_date = Column(Date)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime)

    def __str__(self):
        return f'@{self.username}' if self.username else self.first_name


@event.listens_for(JigasyaMember, 'before_update')
def update_updated_at(mapper, connection, target):
    target.updated_at = datetime.utcnow()
