from ninja import Schema


class UserSchemaStore(Schema):
    email: str
    username: str
    password: str


class UserSchema(Schema):
    email: str
    username: str


class UserSchemaAuth(Schema):
    username: str
    password: str
