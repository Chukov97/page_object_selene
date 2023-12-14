import dataclasses
from demoqa_tests.enums.gender import Gender
from demoqa_tests.enums.hobby import Hobby


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    year: str
    month: str
    day: str
    subject: str
    hobby: Hobby
    picture: str
    address: str
    state: str
    city: str


user = User(
    first_name='Ivan',
    last_name='Ivanov',
    email='ivanov@gmail.com',
    gender=Gender.FEMALE,
    phone_number='9100000001',
    year='1997',
    month='August',
    day='11',
    subject='Commerce',
    hobby=Hobby.SPORTS,
    picture='picture.png',
    address='132, My Street, Bigtown BG23 4YZ',
    state='NCR',
    city='Noida'
)
