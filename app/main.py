import sys
import os

# カレントディレクトリを検索パスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import Session
from db_setting.db_base import SessionLocal
from models.user import User
from models.user2 import User2
import logging

root_logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
handler.setLevel(logging.DEBUG)
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

# セッションを取得
db = SessionLocal()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).all()

def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, user_id: int, name: str, age: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        user.age = age
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

# CRUD操作の例
new_user = User(name="John Doe", age=30)
create_user(db, new_user)

users = get_users(db)
logger.info("作成直後")
logger.info(users)

user = get_user(db, new_user.id)
logger.info("変更前")
logger.info(user)

update_user(db, new_user.id, name="Jane Doe", age=25)
user = get_user(db, new_user.id)
logger.info("変更後")
logger.info(user)
# delete_user(db, new_user.id)

db.close()
