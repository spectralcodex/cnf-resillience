from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class Student(BaseModel):
    id: int
    name: str = Field(None, title="name of student", max_length=10)
    subjects: List[str] = []


@router.post("/students/")
async def student_data(s1: Student):
    return s1
