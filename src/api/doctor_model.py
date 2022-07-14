from pydantic import BaseModel


class DoctorModel(BaseModel):
    doctor_name: str
    specialty: str
    hospital_name: str
