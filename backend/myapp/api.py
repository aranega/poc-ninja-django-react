from ninja import NinjaAPI, Router
from .schemas import School, Student
from .models import School as SchoolModel, Student as StudentModel


# This part is not required, it is here to have custom endpoint names
# and to apply automatically the "by_alias" to each registered endpoint
class MyAppAPI(NinjaAPI):

    def get_openapi_operation_id(self, operation):
        return operation.view_func.__name__


# to avoid the redundant "by_alias=True", not the best though
class MyRouter(Router):
    def api_operation(self, *args, **kwargs):
        kwargs["by_alias"] = True
        return super().api_operation(*args, **kwargs)


api = MyAppAPI(title="myapp", default_router=MyRouter())


@api.get("/schools", response=list[School], tags=["school"])
def get_schools(request):
    return SchoolModel.objects.all()


@api.get("/schools/{name}", response=School | None, tags=["school"])
def get_school(request, name: str):
    return SchoolModel.objects.filter(name=name).first()


@api.get("/schools/{name}/students", response=list[Student], tags=["school"])
def get_school_student(request, name: str):
    return SchoolModel.objects.filter(name=name).first().students
    # return StudentModel.objects.filter(school__name=name)  # Otherwise, slightly different


@api.post("/schools/{schoolName}/students", response=Student, tags=["school"])
def create_student(request, schoolName: str, student: Student):
    school = SchoolModel.objects.filter(name=schoolName).first()
    s = StudentModel(school=school, **student.dict())
    s.save()
    return s


@api.get("/students", response=list[Student], tags=["students"])
def get_students(request):
    return StudentModel.objects.all()


@api.get("/students/{firstName}", response=list[Student], tags=["students"])
def get_student(request, firstName: str):
    return StudentModel.objects.filter(first_name=firstName).first()


@api.get("/students/{firstName}/school", response=list[Student], tags=["students"])
def get_student_school(request, firstName: str):
    return StudentModel.objects.filter(first_name=firstName).first().school


# Ugly, only here to populate the db
@api.post("/generate")
def create_schools(request) -> str:
    school = SchoolModel(name="SCHOOL1")
    s1 = StudentModel(first_name="A", last_name="A", age=23, school=school)
    s2 = StudentModel(first_name="B", last_name="B", age=45, school=school)
    school.save()
    s1.save()
    s2.save()

    school = SchoolModel(name="SCHOOL2")
    s1 = StudentModel(first_name="C", last_name="C", age=12, school=school)
    s2 = StudentModel(first_name="D", last_name="D", age=67, school=school)
    school.save()
    s1.save()
    s2.save()
    return "OK"
