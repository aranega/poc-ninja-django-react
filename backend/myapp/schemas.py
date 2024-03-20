from .utils import BilingualSchema


class Student(BilingualSchema):
    first_name: str
    last_name: str
    age: int


class School(BilingualSchema):
    name: str
    students: list[Student]