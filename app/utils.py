from passlib.context import CryptContext                         #    OAuth

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # OAuth

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)