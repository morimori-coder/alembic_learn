import sys
import os

# カレントディレクトリを検索パスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.orm import Session
from db_setting.db_base import SessionLocal
from models.user import User
from models.user2 import User2
# データベースの初期化
# init_db()

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
print("作成直後")
print(users)

user = get_user(db, new_user.id)
print("変更前")
print(user)

update_user(db, new_user.id, name="Jane Doe", age=25)
user = get_user(db, new_user.id)
print("変更後")
print(user)
# delete_user(db, new_user.id)

db.close()
