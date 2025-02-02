from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, ForeignKey

from database.main_db.database import Base


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    group = Column(Integer, ForeignKey('groups.id'), nullable=False)
    telegram_id = Column(Integer, nullable=True, unique=True)

    def __repr__(self) ->str:
        return f'Student [ID: {self.id}, ФИО: {self.full_name}, grID: {self.group}, TgID: {self.telegram_id}]'



@dataclass
class StudentRaw:
    full_name:str
