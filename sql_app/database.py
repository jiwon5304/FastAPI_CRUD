import os
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# mysql 연결
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/fastapi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# 1. SQLite 데이터베이스 사용 시
# ./sql_app.db -> 파일의 동일한 디렉토리
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# 2. postgresql 데이터베이스 사용 시
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 추후 클래스를 상속받아 데이터베이스의 모델이나 ORM 클래스를 생성
Base = declarative_base()