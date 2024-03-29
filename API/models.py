from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User (Base) :

    __tablename__ = "users"

    id = Column (Integer, 
                 primary_key = True)
    
    email = Column (String, 
                    unique = True, 
                    index = True)
    
    password = Column (String)
    
    is_active = Column (Boolean, 
                        default = True)

    articles = relationship ("Article", 
                             back_populates = "owner")

class Article (Base) :
    
    __tablename__ = "articles"

    id = Column (Integer, 
                 primary_key = True)
    
    title = Column (String, 
                    index = True)

    description = Column (String, 
                          index = True)
    
    owner_id = Column (Integer, 
                       ForeignKey ("users.id"))

    owner = relationship ("User", 
                          back_populates = "articles")