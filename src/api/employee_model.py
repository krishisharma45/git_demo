from pydantic import BaseModel


class EmployeeModel(BaseModel):
    name: str
    age: int
    title: str
    salary: int