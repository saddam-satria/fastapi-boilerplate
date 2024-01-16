from sqlalchemy import Column, String, DateTime,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.sql import func



Base = declarative_base()

class UserCredential(Base):
    __tablename__="UserCredential"
    userCredentialId=Column(String(255), primary_key=True,autoincrement=False)
    email= Column(String(255), unique=True)
    password= Column(String(255))
    isDeleted = Column(Boolean)
    createdAt = Column(DateTime(timezone=True),server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now(),onupdate=func.now())


    def __init__(self, email,password):
        self.userCredentialId = uuid.uuid4()
        self.email = email
        self.password = password
        

    def __repr__(self):
        return f"{self.email} {self.password} {self.userCredentialId} {self.createdAt} {self.updatedAt} {self.isDeleted}"