from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from .database import Base

## SQLAlchemy models
# 이전에 만든 Base를 상속받아 SQLAlchemy 모델 생성
class User(Base):
    
    # 테이블 이름
    __tablename__ = "users"

    # 테이블 열
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(16), unique=True, index=True)
    hashed_password = Column(String(200))
    is_active = Column(Boolean, default=True)

    # relationship 함수를 이용하여 데이터베이스 관계 생성
    items = relationship("Item", back_populates="owner")



class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(20), index=True)
    description = Column(String(20), index=True)
    owner_id = Column(Integer, ForeignKey("users.id")) # 1(user):n(item)

    owner = relationship("User", back_populates="items")