from pydantic import BaseModel


class PatientModel(BaseModel):
    name: str
    age: int
    doctor: str
    diagnosis: int