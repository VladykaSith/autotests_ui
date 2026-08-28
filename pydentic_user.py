from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool=True


user_data={
    "id":1,
    "username":"zara",
    "email":"zara.bond@gmail.com",
    "is_active":False,
}

user=User(**user_data)
print(user.id, user.username, user.email, user.is_active, sep='\n')
