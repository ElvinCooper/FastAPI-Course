import jwt
import datetime

SECRET_KEY = "353e9e4d3377500c183240753b0d7494"

payload: dict = {
    "username": "elvin",
    "email": "elvinexample@g.ocm",
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
}


# creacion del token
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print(token)


