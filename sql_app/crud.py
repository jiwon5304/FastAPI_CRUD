from sqlalchemy.orm import Session
from . import models, schemas


# add: 인스턴스 개체를 데이터베이스 세션에 추가
# commit: 데이터베이스에 변경사항 저장
# refresh: 생성된 id에 새 데이터 포함
# expire: 변경사항 폐기처분

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item: schemas.ItemUpdate, item_id: int):
    # to do: 존재하지 않는 item_id 값이 입력되는 경우 에러처리
    db_item = db.query(models.Item).filter(models.Item.id == item_id).one()
    for (key, value) in item:
        setattr(db_item, key, value)
        db.add(db_item)
        db.commit()     # 변경사항 저장
        # db.refresh(db_item)
    return db_item

def delete_item(db: Session, item: schemas.ItemDelete, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).one()
    db.delete(db_item)
    db.commit()         # 변경사항 저장
    return db_item
