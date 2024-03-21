from ninja import ModelSchema
from .utils import BilingualSchema
from .models import Student as StudentModel, School as SchoolModel


class Student(ModelSchema, BilingualSchema):
    class Meta:
        model = StudentModel
        fields = ["first_name", "last_name", "age"]


class School(ModelSchema, BilingualSchema):
    students: list[Student]

    class Meta:
        model = SchoolModel
        fields = ["name"]


## Other way to do it, without auto-wrapping django models

# class Student(BilingualSchema):
#     first_name: str
#     last_name: str
#     age: int


# class School(BilingualSchema):
#     name: str
#     students: list[Student]
