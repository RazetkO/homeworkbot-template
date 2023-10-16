from pydantic import BaseModel

from model.pydantic.students_group import StudentGroup
from model.pydantic.discipline_works import DisciplinesConfig
from model.pydantic.teacher import Teacher


class DbStartData(BaseModel):
    groups: list[StudentGroup]
    disciplines: list[DisciplinesConfig]
    teachers: list[Teacher]
    chats: list[int]
