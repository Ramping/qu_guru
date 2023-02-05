from dataclasses import dataclass
from enum import Enum
from typing import Literal, List


class Hobby(Enum):
    Sports = 1,
    Reading = 2,
    Music = 3


class Gender(Enum):
    Male = 1,
    Female = 2,
    Other = 3


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: List
    gender: Gender
    subject: Literal['Maths', 'Accounting', 'Arts', 'Social Studies', 'English', 'Chemistry', 'Physics',
    'Computer Science', 'Economics', 'History', 'Civics', 'Commerce', 'Biology', 'Hindi']
    hobby: List[Hobby]
    image: str
    state: Literal['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    city: Literal['Karnal', 'Panipat', 'Delhi', 'Gurgaon', 'Noida', 'Agra', 'Merrut', 'Lucknow', 'Jaipur', 'Jaiselmer']
